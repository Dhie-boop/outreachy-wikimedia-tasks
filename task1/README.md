# JSON Data Formatter

## Description

This is a JavaScript-based HTML page that demonstrates how to manipulate JSON data and display it in a human-readable format. The script processes an array of Wikipedia article metadata and formats it into readable sentences.

## What It Does

The script:

- Takes an array of JSON objects containing Wikipedia article information
- Parses and formats ISO date strings (YYYY-MM-DD) into human-readable format (Month Day, Year)
- Uses `Intl.DateTimeFormat` for locale-aware date formatting
- Handles dates as UTC to ensure consistent output across all timezones
- Generates formatted text for each article
- Displays both the source code and the formatted results on the page

## Data Structure

Each article object contains:

- `page_id`: Wikipedia page ID number
- `creation_date`: Article creation date in ISO format (YYYY-MM-DD)
- `title`: Article title

**Example:**

```json
{"page_id": 6682420, "creation_date": "2021-09-13", "title": "André Baniwa"}
```

## Output Format

Each article is formatted as:

```
Article "TITLE" (Page ID ID) was created at MONTH DAY, YEAR.
```

**Example:**

```
Article "André Baniwa" (Page ID 6682420) was created at September 13, 2021.
```

## Requirements

- A modern web browser (Chrome, Firefox, Safari, Edge, etc.)
- No additional dependencies or installations required
- Works entirely client-side (no server needed)

## How to Use

### Option 1: Double-click to Open

1. Navigate to the `task1` folder
2. Double-click on `Task 1 - Intern.html`
3. The file will open in your default web browser

### Option 2: Open from Browser

1. Open your web browser
2. Press `Ctrl+O` (Windows/Linux) or `Cmd+O` (Mac)
3. Navigate to and select `Task 1 - Intern.html`
4. Click "Open"

### Option 3: Open from VS Code

1. Right-click on `Task 1 - Intern.html` in VS Code
2. Select "Open with Live Server" (if you have the Live Server extension)

   OR

3. Select "Reveal in File Explorer"
4. Double-click the file to open it in your browser

## What You'll See

The page displays two sections:

1. **My code:** Shows the complete JavaScript code used to process the data
2. **Results of my code:** Shows the formatted output with all 12 articles displayed in human-readable format

## Sample Output

When you open the HTML file, you'll see results like:

- Article "André Baniwa" (Page ID 6682420) was created at September 13, 2021.
- Article "Benki Piyãko" (Page ID 4246775) was created at December 10, 2013.
- Article "Célia Xakriabá" (Page ID 5882073) was created at December 3, 2018.
- Article "Chirley Pankará" (Page ID 6977673) was created at October 5, 2022.
- ...and 8 more articles

## Code Features

### Date Formatting Function

- Converts ISO date format (2021-09-13) to readable format (September 13, 2021)
- Uses `Intl.DateTimeFormat` API for locale-aware formatting
- Parses dates as UTC using `Date.UTC()` to prevent timezone offset issues
- Supports easy internationalization by changing the locale parameter
- Ensures consistent date display regardless of user's local timezone

### Benefits of the Implementation

- **No hardcoded month names**: Eliminates potential typos and makes maintenance easier
- **Locale support**: Can easily switch to other languages (e.g., 'pt-BR' for Portuguese)
- **Timezone-safe**: Dates display correctly in all timezones (UTC-3, UTC+5, etc.)

### Dynamic Content Rendering

- Loops through all articles in the data array
- Builds formatted HTML output dynamically
- Injects results into the page using DOM manipulation

### Self-Documenting

- Displays the source code on the page itself
- No need to view source to see how it works

## Files

- `Task 1 - Intern.html` - Main HTML file with embedded JavaScript
- `what-to-do.md` - Task requirements and specifications
- `README.md` - This documentation file

## Technical Details

- **Language:** JavaScript (ES6+)
- **DOM Methods Used:** 
  - `document.getElementById()`
  - `.innerHTML` property
  - `.innerText` property
- **JavaScript Features:**
  - Arrow functions
  - Template literals
  - Array methods (forEach)
  - Date object manipulation

## Customization

To add more articles or modify the data:

1. Open `Task 1 - Intern.html` in a text editor
2. Find the `data` array in the script section
3. Add new objects following this format:

   ```javascript
   {"page_id": 1234567, "creation_date": "YYYY-MM-DD", "title": "Article Title"}
   ```

4. Save and refresh the page in your browser

## Browser Compatibility

Works in all modern browsers that support:

- ES6 JavaScript (2015+)
- DOM manipulation
- Arrow functions
- Template literals

Compatible with:

- Chrome/Edge 51+
- Firefox 54+
- Safari 10+
- Opera 38+
