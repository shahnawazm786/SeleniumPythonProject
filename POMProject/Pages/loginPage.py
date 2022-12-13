from selenium.webdriver.common.by import By
from POMProject.Locators.locators import Locators

class LoginPage:


    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(By.ID, Locators.username_textbox_id).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(By.ID, Locators.password_textbox_id).send_keys(password)
    def click_loginbutton(self):
        self.driver.find_element(By.ID, Locators.login_button_id).click()

    def invalid_login_message(self):
        msg=self.driver.find_element(By.XPATH,Locators.invvalid_login_message_xpath).text
        return msg



