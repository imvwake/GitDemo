import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

service_obj = Service("Users/vivekroshan.marwal/Downloads/edgedriver_win32")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '//input[@class="search-keyword"]').send_keys("ber")
time.sleep(2)
res = driver.find_elements(By.XPATH, "//div[@class='products']/div")
r1=len(res)
for rrr in res:
    rrr.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

driver.find_element(By.XPATH," //button[normalize-space()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH," //input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum=0
print(prices)
for price in prices:
    sum = sum + int(price.text)
print(sum)

wait = WebDriverWait(driver, 15)
time.sleep(10)
totalamount = int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)
print(totalamount)
assert sum == totalamount
#kmfkvmkfnvjfn
