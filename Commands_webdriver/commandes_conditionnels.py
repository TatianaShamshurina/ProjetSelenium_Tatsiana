import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(4)
check_selected_element = driver.find_element(By.ID,'checkbox2').is_selected()       #check li checkbox - true false
print(check_selected_element)

check_button_enabled = driver.find_element(By.ID,'but1').is_enabled()      #check if button is enable
print(check_button_enabled)

check_element_displayed = driver.find_element(By.ID,'hbutton').is_displayed()      #check if element is displayed
print(check_element_displayed)

driver.close()

