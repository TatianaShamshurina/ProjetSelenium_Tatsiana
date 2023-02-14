import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.get("http://localhost:8084/login.php")          #perexodit s odnogo url na drugoi cherez 4 sec
time.sleep(4)
driver.back()           #perexodit na pervyi site
time.sleep(4)
driver.forward()    #idet na vtoroi site
time.sleep(4)
driver.refresh()    #refresh vtorogo site       equivalence F5
driver.close()