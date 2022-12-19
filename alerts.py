import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service_obj = Service("Users/vivekroshan.marwal/Downloads/edgedriver_win32")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("ind")
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)

