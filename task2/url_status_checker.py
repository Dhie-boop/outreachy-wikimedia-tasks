import csv
import requests


def get_url_status(url):
    """
    Get the HTTP status code for a given URL.
    
    Args:
        url (str): The URL to check
        
    Returns:
        int: The HTTP status code, or None if request fails
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, timeout=10, headers=headers, verify=True)
        return response.status_code
    except requests.exceptions.RequestException:
        return None


def main():
    """
    Read URLs from CSV file and print their status codes.
    """
    csv_file = 'Task 2 - Intern.csv'
    
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            url = list(row.values())[0] if row else None
            
            if url:
                status_code = get_url_status(url)
                
                if status_code:
                    print(f"({status_code}) {url}")
                else:
                    print(f"(ERROR) {url}")


if __name__ == "__main__":
    main()

