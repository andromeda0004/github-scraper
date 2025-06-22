from selenium import webdriver
from selenium.webdriver.chrome.service import Service

cdp = "/home/kali/Desktop/Chrome Drivers/chromedriver-linux64/chromedriver"
service = Service(executable_path=cdp)
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
driver.quit()