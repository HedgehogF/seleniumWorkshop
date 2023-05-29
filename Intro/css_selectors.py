import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# initializam chrome-ul

driver = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/form")

#1. **Selecting elements by tag name**
driver.find_element(By.CSS_SELECTOR,"input").send_keys("First name")
time.sleep(2)

#2. **Selecting elements by attribute**:
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").send_keys("Last name")
time.sleep(2)

#3. **Selecting elements by attribute presence**:
driver.find_element(By.CSS_SELECTOR,"input[aria-label]']").click()
time.sleep(2)

#4. **Selecting elements by attribute partial match**:
driver.find_element(By.CSS_SELECTOR,"input[placeholder*='job-title']']").click()
time.sleep(2)

# 5. **Selecting elements by position**:
driver.find_element(By.CSS_SELECTOR,"input:nth-child(1)]").click()
time.sleep(2)

# 6. **Selecting elements based on the relationship with other elements**:
driver.find_element(By.CSS_SELECTOR,"form>div>div>input").click()
time.sleep(2)

# 7. **Selecting elements based on multiple criteria**:
driver.find_element(By.CSS_SELECTOR,"input[type='text'][placeholder='mm/dd/yyyy']").click()
time.sleep(2)

#8. **Selecting elements using wildcard**:
driver.find_element(By.CSS_SELECTOR,"input[placeholder^='Enter your job']").click()
time.sleep(2)

driver.quit()