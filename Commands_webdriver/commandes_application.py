#ces commandes sont liees a l<application du test
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

title_of_page = driver.title
print(title_of_page)

url_of_page = driver.current_url
print(url_of_page)

code_surce_page = driver.page_source
print(code_surce_page)
time.sleep(4)
driver.close()

