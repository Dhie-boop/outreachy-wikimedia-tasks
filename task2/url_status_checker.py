"""
URL Status Checker - A tool to check HTTP status codes for URLs from a CSV file.

This script reads URLs from a CSV file and checks their HTTP status codes,
with support for retries, concurrent processing, and detailed error reporting.
"""

import argparse
import csv
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class URLStatusChecker:
    """Handles URL status checking with retry logic and session management."""
    
    def __init__(self, timeout: int = 10, max_retries: int = 3):
        """
        Initialize the URL status checker.
        
        Args:
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts for failed requests
        """
        self.timeout = timeout
        self.session = self._create_session(max_retries)
    
    def _create_session(self, max_retries: int) -> requests.Session:
        """Create a requests session with retry logic."""
        session = requests.Session()
        
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "HEAD"]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        })
        
        return session
    
    def check_url(self, url: str) -> Tuple[str, Optional[int], Optional[str]]:
        """
        Check the HTTP status code for a given URL.
        
        Args:
            url: The URL to check
            
        Returns:
            Tuple of (url, status_code, error_message)
        """
        if not url or not url.strip():
            return url, None, "Empty URL"
        
        url = url.strip()
        
        # Validate URL format
        try:
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                return url, None, "Invalid URL format"
        except Exception as e:
            return url, None, f"URL parse error: {str(e)}"
        
        try:
            response = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            return url, response.status_code, None
            
        except requests.exceptions.Timeout:
            return url, None, "Request timeout"
        except requests.exceptions.ConnectionError:
            return url, None, "Connection error"
        except requests.exceptions.TooManyRedirects:
            return url, None, "Too many redirects"
        except requests.exceptions.SSLError:
            return url, None, "SSL certificate error"
        except requests.exceptions.RequestException as e:
            return url, None, f"Request error: {str(e)}"
        except Exception as e:
            return url, None, f"Unexpected error: {str(e)}"
    
    def close(self):
        """Close the session."""
        self.session.close()


def read_urls_from_csv(csv_file: str) -> list[str]:
    """
    Read URLs from a CSV file.
    
    Args:
        csv_file: Path to the CSV file
        
    Returns:
        List of URLs
        
    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        ValueError: If the CSV file is empty or invalid
    """
    file_path = Path(csv_file)
    
    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_file}")
    
    urls = []
    
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file)
            
            if not csv_reader.fieldnames:
                raise ValueError("CSV file appears to be empty")
            
            for row_num, row in enumerate(csv_reader, start=2):  
                if row:
                    url = next((v.strip() for v in row.values() if v and v.strip()), None)
                    if url:
                        urls.append(url)
                    
    except csv.Error as e:
        raise ValueError(f"Error reading CSV file: {e}")
    
    if not urls:
        raise ValueError("No URLs found in CSV file")
    
    return urls


def check_urls_sequential(urls: list[str], checker: URLStatusChecker, 
                          output_file: Optional[str] = None) -> dict:
    """
    Check URLs sequentially and display results.
    
    Args:
        urls: List of URLs to check
        checker: URLStatusChecker instance
        output_file: Optional file path to save results
        
    Returns:
        Dictionary with statistics
    """
    results = []
    stats = {"total": len(urls), "success": 0, "failed": 0}
    
    print(f"\nChecking {len(urls)} URLs...\n")
    
    for i, url in enumerate(urls, 1):
        url_result, status_code, error_msg = checker.check_url(url)
        
        if status_code:
            output = f"({status_code}) {url_result}"
            stats["success"] += 1
        else:
            output = f"(ERROR: {error_msg}) {url_result}"
            stats["failed"] += 1
        
        print(f"[{i}/{len(urls)}] {output}")
        results.append(output)
    
    
    if output_file:
        save_results(output_file, results)
    
    return stats


def check_urls_concurrent(urls: list[str], checker: URLStatusChecker, 
                          max_workers: int = 10, 
                          output_file: Optional[str] = None) -> dict:
    """
    Check URLs concurrently using ThreadPoolExecutor.
    
    Args:
        urls: List of URLs to check
        checker: URLStatusChecker instance
        max_workers: Maximum number of concurrent workers
        output_file: Optional file path to save results
        
    Returns:
        Dictionary with statistics
    """
    results = []
    stats = {"total": len(urls), "success": 0, "failed": 0}
    completed = 0
    
    print(f"\nChecking {len(urls)} URLs concurrently (max {max_workers} workers)...\n")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(checker.check_url, url): url for url in urls}
        
        for future in as_completed(future_to_url):
            completed += 1
            url_result, status_code, error_msg = future.result()
            
            if status_code:
                output = f"({status_code}) {url_result}"
                stats["success"] += 1
            else:
                output = f"(ERROR: {error_msg}) {url_result}"
                stats["failed"] += 1
            
            print(f"[{completed}/{len(urls)}] {output}")
            results.append(output)
    
    
    if output_file:
        save_results(output_file, results)
    
    return stats


def save_results(output_file: str, results: list[str]):
    """Save results to a file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(results))
        print(f"\n✓ Results saved to: {output_file}")
    except Exception as e:
        print(f"\n✗ Error saving results: {e}", file=sys.stderr)


def print_statistics(stats: dict):
    """Print summary statistics."""
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total URLs checked: {stats['total']}")
    print(f"Successful: {stats['success']} ({stats['success']/stats['total']*100:.1f}%)")
    print(f"Failed: {stats['failed']} ({stats['failed']/stats['total']*100:.1f}%)")
    print("=" * 50)


def main():
    """Main entry point for the URL status checker."""
    parser = argparse.ArgumentParser(
        description="Check HTTP status codes for URLs from a CSV file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    
  %(prog)s -f urls.csv                        
  %(prog)s --concurrent --workers 20          
  %(prog)s -o results.txt                     
  %(prog)s -f urls.csv -o results.txt --concurrent
        """
    )
    
    parser.add_argument(
        '-f', '--file',
        default='Task 2 - Intern.csv',
        help='CSV file containing URLs (default: Task 2 - Intern.csv)'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Save results to output file'
    )
    
    parser.add_argument(
        '--concurrent',
        action='store_true',
        help='Enable concurrent processing for faster checks'
    )
    
    parser.add_argument(
        '--workers',
        type=int,
        default=10,
        help='Number of concurrent workers (default: 10)'
    )
    
    parser.add_argument(
        '--timeout',
        type=int,
        default=10,
        help='Request timeout in seconds (default: 10)'
    )
    
    parser.add_argument(
        '--retries',
        type=int,
        default=3,
        help='Maximum retry attempts (default: 3)'
    )
    
    args = parser.parse_args()
    
    try:
        
        urls = read_urls_from_csv(args.file)
        
        
        checker = URLStatusChecker(timeout=args.timeout, max_retries=args.retries)
        
        try:
            
            if args.concurrent:
                stats = check_urls_concurrent(urls, checker, args.workers, args.output)
            else:
                stats = check_urls_sequential(urls, checker, args.output)
            
            
            print_statistics(stats)
            
        finally:
            checker.close()
            
    except FileNotFoundError as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n✗ Interrupted by user", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
