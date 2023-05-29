
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver  = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/autocomplete")


# The implicitly_wait is set to 0, so here if the element is not find it will throw instant exception (NoSuchElementException)
driver.find_element(By.CSS_SELECTOR,"input#autocomplete").send_keys("Address")

# Starting with this line our program will wait maxim 3 seconds for the element, if the element is not displayed in 3 second will throw an exception (NoSuchElementException)
driver.implicitly_wait(3)

driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys("Address")


# Explicit wait
# Asteptam maxim 15 de secunde strict dupa elementul cu id-ul 'checkbox-12'
check_box = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID,"checkbox-12")))

check_box.click()


