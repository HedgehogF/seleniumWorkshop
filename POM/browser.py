from selenium import webdriver


class Browser:

    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.set_page_load_timeout(5)

    def close(self):
        self.driver.quit()