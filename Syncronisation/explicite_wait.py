# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#driver.implicitly_wait(20)      #mechanisme wait global dinamic quand on a ine page lourd
my_wait=WebDriverWait(driver,20)
driver.get("https://www.google.com")
time.sleep(4)
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys('selenium')
#driver.find_element(By.NAME,'q').send_keys("selenium")
search_google=my_wait.until(EC.presence_of_element_located((By.NAME,'q')))
#search_google = driver.find_element(By.NAME,'q')
search_google.send_keys("selenium")
search_google.submit()
lien_result = driver.find_element(By.XPATH,'//h3[text()="Selenium"]')
lien_result.click()
time.sleep(3)
driver.close()