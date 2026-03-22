# URL Status Checker

## Description

This is a Python script that reads a list of URLs from a CSV file and retrieves the HTTP status code for each URL. The script prints the results in a formatted output showing the status code alongside each URL.

## What It Does

The script:

- Reads URLs from `Task 2 - Intern.csv`
- Makes HTTP GET requests to each URL
- Retrieves and displays the HTTP status code for each URL
- Handles errors gracefully for unreachable or invalid URLs
- Uses a browser User-Agent header to improve compatibility with websites

## Output Format

The script prints results in the following format:

```
(STATUS_CODE) URL
```

**Examples:**

- `(200) https://juanfutbol.com` - Success
- `(404) https://gshow.globo.com/programas/mais-voce/v2011/MaisVoce/0` - Not Found
- `(403) https://www.worldfootball.net/team_performance/kosovo-frauen-team/frauen-wm-quali-europa-2017-2018` - Forbidden
- `(ERROR) https://www.uefa.com/teamsandplayers/players/player=250107154/profile` - Connection/DNS Error
- `(500)  https://br.search.yahoo.com/?fr2=p:sportsrd` - Internal Server Error
- `(503)  https://www.espn.com.br/blogs/espnw/730784_eu-uma-das-100-mulheres-mais-influentes-do-mundo` - Service Unavailable

## Requirements

- Python 3.6 or higher
- `requests` library
- `types-requests` (for type checking)

## Installation

### 1. Create a Virtual Environment

```bash
# Navigate to the task2 directory
cd task2

# Create your virtual environment 
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install the requests library
pip install -r requirements.txt

```

### 3. Verify Installation

```bash
# Check installed packages
pip list
```

You should see `requests` and `urllib3` in the list.

## Usage

1. Ensure your virtual environment is activated
2. Make sure `Task 2 - Intern.csv` is in the same directory as the script
3. Run the script:

```bash
python url_status_checker.py
```

## Expected Output

The script will print status codes for all URLs in the CSV file. Some URLs may show `(ERROR)` if they are:

- No longer active/online
- Blocking automated requests
- Have DNS resolution issues
- Have SSL/TLS certificate problems

This is expected behavior for old or inactive URLs.

## Files

- `url_status_checker.py` - Main Python script
- `Task 2 - Intern.csv` - Input file containing URLs
- `requirements.txt` - List of project dependencies
- `README.md` - This documentation file

## Notes

- The script includes a 10-second timeout for each request
- Uses UTF-8-BOM encoding to handle CSV files properly
- Includes a User-Agent header to prevent blocking by some websites
- Error handling ensures the script continues even if individual URLs fail
