import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# a partir d ici = testlink

driver.get("http://localhost:8084/login.php")
driver.find_element(By.NAME,"tl_login").send_keys("6121951")
driver.find_element(By.NAME,"tl_password").send_keys("T@ni@testlink1!")
driver.find_element(By.XPATH,"//div[3]").click()
time.sleep(5)
general_frame_TL = driver.find_elements(By.TAG_NAME,"frameset")
print(len(general_frame_TL))

driver.find_elements(By.TAG_NAME,'frameset')
'''list_frame=driver.find_elements(By.XPATH,"//frame[@name='mainframe']")
print(len(list_frame))
#driver.find_element(By.XPATH,"//span[contains(text(),'Campagne-Goupe3')]").click()
time.sleep(4)
# find Elements
#tous les lien de la page
list_frame=driver.find_elements(By.XPATH,"//frame[@name='mainframe']")
print(len(list_frame))


list_a=driver.find_elements(By.XPATH,"//a")
print(len(list_a))

list_liens = driver.find_elements(By.TAG_NAME,'a')              #daet spisok linkov
print(len(list_liens))
for link in list_liens:
    print(link.get_attribute("href"))

# console:
$x("//a")
(17) [a.chosen-single, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item, a.list-group-item]
0:a.chosen-single
1:a.list-group-item
2:a.list-group-item
3:a.list-group-item
4:a.list-group-item
5:a.list-group-item
6:a.list-group-item
7:a.list-group-item
8:a.list-group-item
9:a.list-group-item
10:a.list-group-item
11:a.list-group-item
12:a.list-group-item
13:a.list-group-item
14:a.list-group-item
15:a.list-group-item
16:a.list-group-item
length:17
time.sleep(4)
driver.close()'''