# Outreachy Wikimedia Tasks - Lusophone Technological Wishlist

## About the Lusophone Technological Wishlist

The Lusophone technological wishlist is a community-driven survey conducted within Portuguese-speaking Wikimedia projects to identify and prioritize technological innovations, tools, and platform modifications that could improve the user experience for editors, readers, and researchers. This initiative aligns with the WMF Annual Plan Products & Technology bucket for Wiki Experiences.

The project aims to implement community wishes, specifically:

- **Wishlist #3**: Implement a check in the Visual Editor for duplicate references using identifiers (ISBN, DOI, or URL), allowing users to reuse existing references
- **Wishlist #8**: Implement Wikidata support for Wikimedia Brasil's scoring tool (wikiscore) to enable edit-a-thons and edit contests using Wikidata

## Repository Structure

```
outreachy-wikimedia-tasks/
├── task1/                      # Task 1 - JSON Data Formatter
│   ├── Task 1 - Intern.html   # HTML file with JavaScript
│   ├── README.md              # Task 1 documentation
│
├── task2/                      # Task 2 - URL Status Checker
│   ├── url_status_checker.py  # Python script
│   ├── Task 2 - Intern.csv    # Input CSV with URLs
│   ├── requirements.txt       # Python dependencies
│   ├── README.md              # Task 2 documentation
│
├── .gitignore                 # Git ignore configurations
└── README.md                  # This file
```

---

## Task 1: JSON Data Formatter

### Description

A JavaScript-based HTML page that manipulates JSON data containing Wikipedia article metadata and displays it in human-readable format.

### What It Does

- Processes an array of JSON objects with Wikipedia article information
- Converts ISO date strings (YYYY-MM-DD) to readable format (Month Day, Year)
- Uses `Intl.DateTimeFormat` for locale-aware, timezone-safe date formatting
- Generates formatted sentences for each article
- Displays results dynamically on the webpage

### Installation & Setup

**Requirements:**

- A modern web browser (Chrome, Firefox, Safari, Edge)
- No additional installations needed

**How to Run:**

1. Navigate to the `task1` folder
2. Open `Task 1 - Intern.html` in your web browser:
   - **Option A**: Double-click the file
   - **Option B**: Right-click → "Open with" → Select your browser
   - **Option C**: Drag and drop into an open browser window

### Example Output

**Input Data:**
```json
{"page_id": 6682420, "creation_date": "2021-09-13", "title": "André Baniwa"}
```

**Formatted Output:**
```
Article "André Baniwa" (Page ID 6682420) was created at September 13, 2021.
Article "Benki Piyãko" (Page ID 4246775) was created at December 10, 2013.
Article "Célia Xakriabá" (Page ID 5882073) was created at December 3, 2018.
Article "Chirley Pankará" (Page ID 6977673) was created at October 5, 2022.
Article "Cristine Takuá" (Page ID 7069044) was created at February 16, 2023.
...and 7 more articles
```

### Technologies Used

- JavaScript (ES6+)
- HTML5
- DOM manipulation
- `Intl.DateTimeFormat` API for locale-aware date formatting

---

## Task 2: URL Status Checker

### Description

A simple Python script that reads URLs from a CSV file and retrieves the HTTP status code for each URL, displaying results in a formatted output. The script is straightforward and focused (47 lines), without complex CLI features.

### What It Does

- Reads URLs from `Task 2 - Intern.csv`
- Makes HTTP GET requests to each URL
- Retrieves and displays HTTP status codes
- Handles errors gracefully for unreachable URLs
- Includes browser User-Agent header for better compatibility

### Installation & Setup

**Requirements:**

- Python 3.6 or higher
- `requests` library

**Step 1: Create a Virtual Environment**

```bash
# Navigate to the task2 directory
cd task2

# Create virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
task2\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

**Step 2: Install Dependencies**

```bash
# Install required packages
pip install -r requirements.txt

# Or install manually:
pip install requests
```

**Step 3: Run the Script**

```bash
python url_status_checker.py
```

### Example Output

```
(200) http://sportv.globo.com/site/noticia/2011/11/em-casa-sao-jose-vence-colo-colo-e-e-campeao-da-libertadores-feminina.html
(200) https://ge.globo.com/futebol/selecao-brasileira/noticia/2023/06/27/convocadas-do-brasil-para-copa-do-mundo-2023-veja-a-lista-de-pia.ghtml
(404) http://www.ecuafutbol.org/copa_america/team.aspx?ID=BRA
(403) http://www.espn.com.br/noticia/556235_ferroviaria-vence-colo-colo-por-3-a-1-e-conquista-libertadores-feminina
(500) https://agenciabrasil.ebc.com.br/esportes/noticia/2020-02/bia-zaneratto-chega-ao-palmeiras-em-momento-magico-do-futebol-feminino
(ERROR) http://jogandocomelas.com.br/rosana-augusto-jogadora-do-santos-e-da-selecao-brasileira-anuncia-aposentadoria/
(200) https://www.cbf.com.br/futebol-brasileiro/noticias/campeonato-brasileiro-feminino/bia-zaneratto-e-eleita-a-jogadora-do-mes-de-maio-do-brasileirao-femini
```

**Status Code Meanings:**

- `200` - Success (page found)
- `403` - Forbidden (access denied)
- `404` - Not Found (page doesn't exist)
- `500` - Internal Server Error
- `ERROR` - Network error (DNS failure, timeout, SSL error, etc.)

### Technologies Used

- Python 3
- `requests` library for HTTP requests
- `csv` module for file parsing
- Simple error handling for network issues

### Key Features

- Simple, focused implementation without complex CLI features
- 10-second timeout for each request
- Browser User-Agent header for better website compatibility
- Graceful error handling for connection failures

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Dhie-boop/outreachy-wikimedia-tasks.git
cd outreachy-wikimedia-tasks
```

### Quick Start Guide

**For Task 1 (JavaScript):**
```bash
cd task1
# Open Task 1 - Intern.html in your browser
```

**For Task 2 (Python):**
```bash
cd task2
python -m venv venv
task2\Scripts\activate  # Windows
pip install -r requirements.txt
python url_status_checker.py
```
