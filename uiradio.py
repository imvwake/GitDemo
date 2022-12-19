import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service_obj = Service("Users/vivekroshan.marwal/Downloads/edgedriver_win32")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

x = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(x))

for x1 in x:
    if x1.get_attribute("value") == "radio2":
        x1.click()
        break
time.sleep(2)