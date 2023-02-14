import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)

placeholder_text = (driver.find_element(By.XPATH,'//input[@name="username"]').get_attribute("placeholder"))
print(placeholder_text)
list_liens = driver.find_elements(By.TAG_NAME,'a')              #daet spisok linkov
print(len(list_liens))

for link in list_liens:
    print(link.get_attribute("href"))

print(link.get_attribute("href")[4])
driver.close()