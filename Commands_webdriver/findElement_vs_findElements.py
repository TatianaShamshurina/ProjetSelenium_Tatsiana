import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button").click()                # Zaloginilis'
time.sleep(4)

#find elements
                                                            #cherche moi tous les elements 'a'
list_tagname_a = driver.find_elements(By.TAG_NAME,"a")      #vse chto est' tagname a = to est linki (list array)
print(len(list_tagname_a))
time.sleep(4)
print("Le text du premier lien est: ",list_tagname_a[3].text)    #vyvesti na pechat text pervogo elementa iz spiska
for a in list_tagname_a:
    print(a.text)
print("Le text du premier lien est: ",list_tagname_a[5].text)
time.sleep(4)
driver.close()