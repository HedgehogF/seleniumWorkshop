from POM.browser import Browser


class BasePage(Browser):

    def navigate_to_page(self,link):
        self.driver.get(link)