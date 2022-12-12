from selenium.webdriver.common.by import By
from POMProject.Locators.locators import Locators
class HomePage:

    def __init__(self,driver):
        self.driver=driver


    def click_on_home_burger_menu(self):
        self.driver.find_element(By.ID, Locators.home_burger_menu_id).click()

    def click_on_logout(self):
        self.driver.find_element(By.ID, Locators.logout_link_id).click()

