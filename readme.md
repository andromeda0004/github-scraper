````markdown
# GitHub Sensitive Keyword Scanner

This Python script scans files in a specified GitHub repository for sensitive keywords using Selenium and ChromeDriver.

## Features

- Accepts a GitHub repository URL from the user
- Scans only root-level files
- Detects keywords: `password`, `token`, `key`, `keys`, `_key`, `_keys`
- Prints the blob page URL where a sensitive keyword is found
- Ignores links like `Packages` and `Releases`
- Does not print the file content

## Requirements

- Python 3.x
- Google Chrome
- ChromeDriver (matching your Chrome version)
- Python library:
  ```bash
  pip install selenium
````

## How to Use

1. Clone the repository or copy the script.
2. Edit the path to your ChromeDriver:

   ```python
   cdp = "/home/kali/Desktop/Chrome Drivers/chromedriver-linux64/chromedriver"
   ```
3. Run the script:

   ```bash
   python3 scanner.py
   ```
4. Enter the GitHub repo URL when prompted.

## Supported File Extensions

* .py
* .js
* .html
* .css
* .c
* .cpp
* .env

## How It Works

* Loads the given GitHub repository
* Extracts all file links from the main page
* Filters files by extension
* Visits the blob page of each valid file
* Opens the raw version of the file
* Scans its content for any of the defined keywords
* Prints the blob page URL if a keyword is found

## Example

```
Enter GitHub repo URL (e.g., https://github.com/user/repo): https://github.com/Test-Account1989/sample-repo
sensitive keyword 'token' found in: https://github.com/Test-Account1989/sample-repo/blob/main/app.js
sensitive keyword 'password' found in: https://github.com/Test-Account1989/sample-repo/blob/main/.env
```

```
```
