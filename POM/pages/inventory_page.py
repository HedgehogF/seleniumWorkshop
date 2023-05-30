from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


class InventoryPage(BasePage):

    PRODUCTS_TITLE = (By.CLASS_NAME,"title")
    PROBLEM_USER_IMAGE = (By.CSS_SELECTOR,"img[src='/static/media/sl-404.168b1cce.jpg']")

    def get_products_title(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE)

    def get_product_problem_image(self):
        return self.driver.find_element(*self.PROBLEM_USER_IMAGE)