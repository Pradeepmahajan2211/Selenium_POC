from selenium.webdriver.common.by import By
import allure

@allure.story("Login")
class LoginPage:
    driver = ''

    def __init__(self, driver):
        self.driver = driver

    loginbtn = (By.XPATH, "//a[@href='/login']")
    usernameInput = (By.ID, "Email")
    passwordInput = (By.ID, "Password")
    log_in_btn = (By.XPATH, "(//input[@type='submit'])[2]")


    def loginbtnOption(self):
        return self.driver.find_element(*LoginPage.loginbtn)

    def usernameInputOption(self):
        return self.driver.find_element(*LoginPage.usernameInput)

    def passwordInputOption(self):
        return self.driver.find_element(*LoginPage.passwordInput)

    def log_in_btnOption(self):
        return self.driver.find_element(*LoginPage.log_in_btn)





