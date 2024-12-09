from selenium.webdriver.common.by import By


class LoginPage:
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
        return self.driver.find_element(*LoginPage.registerbtn)

    def genderInputOption(self):
        return self.driver.find_element(*LoginPage.genderInput)

    def fnameInputOption(self):
        return self.driver.find_element(*LoginPage.fnameInput)

    def LnameInputOption(self):
        return self.driver.find_element(*LoginPage.LnameInput)

    def emailInputOption(self):
        return self.driver.find_element(*LoginPage.emailInput)

    def passwordInputOption(self):
        return self.driver.find_element(*LoginPage.passwordInput)

    def confirmpasswordInputOption(self):
        return self.driver.find_element(*LoginPage.confirmpasswordInput)

    def submitbtninputOption(self):
        return self.driver.find_element(*LoginPage.submitbtninput)







