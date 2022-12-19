import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

service_obj = Service("Users/vivekroshan.marwal/Downloads/edgedriver_win32")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/windows")
driver.implicitly_wait(2)
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowss = driver.window_handles
driver.switch_to.window(windowss[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(20)
#hehfbf