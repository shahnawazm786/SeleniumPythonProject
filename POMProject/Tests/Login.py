from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from POMProject.Pages.loginPage import LoginPage
from POMProject.Pages.homePage import HomePage
import HtmlTestRunner
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #driver = webdriver.Chrome(executable_path='')
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        time.sleep(5)

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/")

        login=LoginPage(driver)
        login.enter_username('standard_user')
        login.enter_password('secret_sauce')
        login.click_loginbutton()
        time.sleep(5)
        home=HomePage(driver)
        home.click_on_home_burger_menu()
        home.click_on_logout()

    def test_login_invalid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.enter_username('standard_user')
        login.enter_password('secret_sauce')
        login.click_loginbutton()
        message=login.invalid_login_message()
        self.assertEqual(message,'Epic sadface: Username and password do not match any user in this service')

        #driver.find_element(By.ID, "user-name").send_keys('standard_user')
        #self.driver.find_element(By.ID, "password").send_keys('secret_sauce')
        #self.driver.find_element(By.ID, "login-button").click()
        #self.driver.find_element(By.ID, 'react-burger-menu-btn').click()

        #self.driver.find_element(By.ID, 'logout_sidebar_link').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("--------------------- Test completed -------------------------")


if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
