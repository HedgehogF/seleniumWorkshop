from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_FIELD = (By.CSS_SELECTOR,"input#user-name")
    PASSWORD_FIELD = (By.CSS_SELECTOR,"input#password")
    LOGIN_BUTTON = (By.XPATH,"//input[@type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR,"h3[data-test='error']")

    def navigate_to_login_page(self):
        self.navigate_to_page("https://www.saucedemo.com/")

    def set_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except NoSuchElementException:
            return 'None'

    def login(self,username,password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()