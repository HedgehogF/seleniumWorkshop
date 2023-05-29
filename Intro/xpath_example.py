import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/autocomplete")

#- Selecting elements by tag name:
driver.find_element(By.XPATH,"//input").send_keys("Address")
time.sleep(2)

#- Selecting elements by attribute:
driver.find_element(By.XPATH, "//input[@type='text']")
time.sleep(2)

#- Selecting elements by attribute presence:
driver.find_element(By.XPATH, "//input[@onfocus]")
time.sleep(2)

#- Selecting elements by attribute partial match:
driver.find_element(By.XPATH, "//input[contains(@class ,'form-control')]")
time.sleep(2)

#- Selecting elements by text content:
driver.find_element(By.XPATH, "//label[text()='Address']")
time.sleep(2)

#- Selecting elements by position:
driver.find_element(By.XPATH, "(//input)[position()=5]")
time.sleep(2)

#- Selecting elements based on the relationship with other elements:
driver.find_element(By.XPATH, "//strong/label")
time.sleep(2)

#- Selecting elements based on multiple criteria:
driver.find_element(By.XPATH," //strong/label[@for='autocomplete' and text()='Address']")
time.sleep(2)


driver.quit()
