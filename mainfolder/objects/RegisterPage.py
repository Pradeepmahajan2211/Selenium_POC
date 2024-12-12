from selenium.webdriver.common.by import By
import allure

@allure.story("Register")
class RegisterPage:
    driver = ''

    def __init__(self, driver):
        self.driver = driver

    registerbtn = (By.XPATH, "//a[contains(text(),'Register')]")
    genderInput = (By.NAME, "Gender")
    fnameInput = (By.NAME, "FirstName")
    LnameInput = (By.NAME, "LastName")
    emailInput = (By.XPATH, "//input[@id='Email']")
    passwordInput = (By.NAME, "Password")
    confirmpasswordInput = (By.NAME, "ConfirmPassword")
    submitbtninput = (By.ID, "register-button")


    def registerbtnOption(self):
        return self.driver.find_element(*RegisterPage.registerbtn)

    def genderInputOption(self):
        return self.driver.find_element(*RegisterPage.genderInput)

    def fnameInputOption(self):
        return self.driver.find_element(*RegisterPage.fnameInput)

    def LnameInputOption(self):
        return self.driver.find_element(*RegisterPage.LnameInput)

    def emailInputOption(self):
        return self.driver.find_element(*RegisterPage.emailInput)

    def passwordInputOption(self):
        return self.driver.find_element(*RegisterPage.passwordInput)

    def confirmpasswordInputOption(self):
        return self.driver.find_element(*RegisterPage.confirmpasswordInput)

    def submitbtninputOption(self):
        return self.driver.find_element(*RegisterPage.submitbtninput)







