class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_xpath = "//a[contains(text(),'Logout')]"

    def click_welcome(self):
        self. driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self. driver.find_element_by_xpath(self.logout_link_xpath).click()