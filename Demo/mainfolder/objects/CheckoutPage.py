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

    billingfname = (By.ID, "BillingNewAddress_FirstName")
    billinglname = (By.ID, "BillingNewAddress_LastName")
    billingEmail = (By.ID, "BillingNewAddress_Email")
    billingcomp = (By.ID, "BillingNewAddress_Company")
    billingcountry = (By.ID, "BillingNewAddress_CountryId")
    billingcity = (By.ID, "BillingNewAddress_City")
    billingadd1 = (By.ID, "BillingNewAddress_Address1")
    billingZip = (By.ID, "BillingNewAddress_ZipPostalCode")
    billingPhone = (By.ID, "BillingNewAddress_PhoneNumber")
    continue2btn = (By.XPATH, "(//input[@title='Continue'])[2]")
    continue3btn = (By.XPATH, "(// input[@ type='button'])[4]")
    continue4btn = (By.XPATH, "(// input[@ type='button'])[5]")
    continue5btn = (By.XPATH, "(// input[@ type='button'])[6]")
    confirmbtn = (By.ID, "confirm-order-please-wait")





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

#after checkout btn

    def billingfnameOption(self):
        return self.driver.find_element(*CheckoutPage.billingfname)

    def billinglnameOption(self):
        return self.driver.find_element(*CheckoutPage.billinglname)

    def billingEmailOption(self):
        return self.driver.find_element(*CheckoutPage.billingEmail)

    def billingcompOption(self):
        return self.driver.find_element(*CheckoutPage.billingcomp)

    def billingcountrypOption(self):
        return self.driver.find_element(*CheckoutPage.billingcountry)

    def billingcityOption(self):
        return self.driver.find_element(*CheckoutPage.billingcity)

    def billingadd1Option(self):
        return self.driver.find_element(*CheckoutPage.billingadd1)

    def billingZipOption(self):
        return self.driver.find_element(*CheckoutPage.billingZip)

    def billingPhoneOption(self):
        return self.driver.find_element(*CheckoutPage.billingPhone)

    def continue2btnOption(self):
        return self.driver.find_element(*CheckoutPage.continue2btn)

    def continue3btnOption(self):
        return self.driver.find_element(*CheckoutPage.continue3btn)

    def continue4btnOption(self):
        return self.driver.find_element(*CheckoutPage.continue4btn)

    def continue5btnOption(self):
        return self.driver.find_element(*CheckoutPage.continue5btn)

    def confirmbtnOption(self):
        return self.driver.find_element(*CheckoutPage.confirmbtn)


