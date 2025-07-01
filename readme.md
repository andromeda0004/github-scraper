# GitHub Sensitive Data Scanner

A lightweight automation tool that crawls a GitHub repository’s file listing and checks for sensitive keywords (like `password`, `token`, or `key`) inside supported files. It uses Selenium WebDriver to dynamically load pages, extract raw file content, and scan for potential credential leaks.

---

## Notable Techniques

* **Dynamic content handling with Selenium**: This project uses [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) to control a Chrome browser instance and interact with dynamically loaded GitHub pages.

* **XPath for element selection**: The [`XPath`](https://developer.mozilla.org/en-US/docs/Web/XPath) query `"//a[normalize-space()='Raw']"` ensures accurate targeting of the “Raw” file button regardless of surrounding HTML structure.

* **Explicit waits using `WebDriverWait` and `expected_conditions`**: Instead of relying on arbitrary delays, the script waits until elements are fully loaded using [`expected_conditions`](https://selenium-python.readthedocs.io/waits.html), improving both performance and reliability.

* **Headless scanning of file listings**: The script loops over visible filenames and filters by extension, simulating how a user would browse and inspect files on GitHub.

---

## Libraries and Technologies

* [Selenium](https://pypi.org/project/selenium/): Used for browser automation and page parsing.
* [Google ChromeDriver](https://sites.google.com/chromium.org/driver/): Required for interfacing with the Chrome browser. Ensure the path is correct for your OS.

> Note: No external UI frameworks, fonts, or front-end libraries are used in this script.

---

## File Reference

* [`main.py`](./main.py): Main script to initiate repo scanning and log sensitive keyword matches.
