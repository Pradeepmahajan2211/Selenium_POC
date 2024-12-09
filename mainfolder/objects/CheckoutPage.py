from selenium.webdriver.common.by import By




class CheckoutPage:
    driver=''

    def __init__(self, driver):
        self.driver = driver

    computerTab = (By.XPATH, "(//a[contains(text(),'Computers')])[1]")
    notebooklink = (By.XPATH, "//img[@title='Show products in category Notebooks']")
    addTocart = (By.XPATH, "//input[@value='Add to cart']")
    shoppingCarbtn = (By.PARTIAL_LINK_TEXT, "Shopping cart")
    country = (By.ID, "CountryId")
    checktermsofservice = (By.NAME, "termsofservice")
    checkout = (By.ID, "checkout")




    def computerTabOption(self):
        return self.driver.find_element(*CheckoutPage.computerTab)

    def notebooklinkOption(self):
        return self.driver.find_element(*CheckoutPage.notebooklink)

    def addTocartOption(self):
        return self.driver.find_element(*CheckoutPage.addTocart)

    def shoppingCarbtnOption(self):
        return self.driver.find_element(*CheckoutPage.shoppingCarbtn)

    def countryOption(self):
        return self.driver.find_element(*CheckoutPage.country)

    def checktermsofserviceOption(self):
        return self.driver.find_element(*CheckoutPage.checktermsofservice)

    def checkoutOption(self):
        return self.driver.find_element(*CheckoutPage.checkout)


