import time
from unittest import TestCase

from selenium.common import NoSuchElementException

from POM.pages.inventory_page import InventoryPage
from POM.pages.login_page import LoginPage


class TestLoginPage(TestCase):

    def setUp(self):
        self.login_page = LoginPage()
        self.inventory_page = InventoryPage()
        self.login_page.navigate_to_login_page()

    def tearDown(self):
        self.login_page.close()


    def test_login_standard_user(self):
        self.login_page.login("standard_user","secret_sauce")
        products_title = self.inventory_page.get_products_title()
        try:
            assert products_title.is_displayed()
        except NoSuchElementException():
            assert False, "No Such element displayed"

    def test_login_locked_out_user(self):
        self.login_page.login("locked_out_user","secret_sauce")
        expected_error_message = "Epic sadface: Sorry, this user has been locked out."
        actual_error_message = self.login_page.get_error_message()
        time.sleep(4)
        self.assertEqual(expected_error_message, actual_error_message, f"The actual message is not the expected one : expected-> {expected_error_message}, actual -> {actual_error_message}")

    def test_login_problem_user(self):
        self.login_page.login("problem_user","secret_sauce")
        image = self.inventory_page.get_product_problem_image()
        try:
            assert image.is_displayed()
        except NoSuchElementException():
            assert False, "No Such element displayed"