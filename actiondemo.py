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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover" )).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(3)