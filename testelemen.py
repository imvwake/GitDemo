import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service_obj = Service("Users/vivekroshan.marwal/Downloads/edgedriver_win32")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
country = driver.find_elements(By.CSS_SELECTOR, "li[class$='ui-menu-item'] a")
print(len(country))
for c1 in country:
    if c1.text == "India":
        c1.click()
        break
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))