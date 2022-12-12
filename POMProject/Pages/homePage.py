from selenium.webdriver.common.by import By

class HomePage:

    def __int__(self,driver):
        self.driver=driver

        self.home_burger_menu_id='react-burger-menu-btn'
        self.logout_link_id='logout_sidebar_link'

    def click_on_home_burger_menu(self):
        self.driver.find_element(By.ID, self.home_burger_menu_id).click()

    def click_on_logout(self):
        self.driver.find_element(By.ID, self.logout_link_id).click()

