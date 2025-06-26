from selenium import webdriver
from selenium.webdriver.chrome.service import Service

my_address = "/home/kali/Desktop/Chrome Drivers/chromedriver-linux64/chromedriver" #this is my address. your path can change.
serv = Service(executable_path=my_address)
driver = webdriver.Chrome(service=serv)

driver.get("https://www.google.com")
driver.quit()
