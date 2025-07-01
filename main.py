from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cdp = "/home/kali/Desktop/Chrome Drivers/chromedriver-linux64/chromedriver" #my address. yours can change

serv = Service(executable_path=cdp)
driver = webdriver.Chrome(service=serv)

repo = input("Enter GitHub repo URL (e.g., https://github.com/user/repo): ").strip()

def raw_page_open(second_page):
	driver.get(second_page)
	try:
		raw_button = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Raw']"))
		)
		raw_url = raw_button.get_attribute("href")
		driver.get(raw_url)
		code = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.TAG_NAME, "pre"))
		).text.lower()

		keywords = ["password", "token", "key", "keys", "_key", "_keys"]
		for word in keywords:
			if word in code:
				print(f"sensitive keyword '{word}' found in: {second_page}")
				break

	except Exception as e:
		print(f"Error: {e}")

def looping(files_page):
	driver.get(files_page)
	elements = driver.find_elements(By.CLASS_NAME, "Link--primary")
	names = [el.text.strip() for el in elements]

	for name in names:
		if name in ["Packages", "Releases"]:
			continue
		if name.endswith(("py", "css", "html", "c", "env", "js", "cpp")):
			second_page = f"{files_page}/blob/main/{name}"
			raw_page_open(second_page)

looping(repo)
driver.quit()
