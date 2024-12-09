import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from mainfolder.objects.CheckoutPage import *
from mainfolder.objects.LoginPage import LoginPage
from mainfolder.utilities.BaseClass import BaseClass
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select



@pytest.mark.usefixtures("setup")
class TestCheckout(BaseClass):
    def test_checkout(self):
        logs = self.get_logger()
        try:
            logs.debug('Browser launched')
            logs.debug('Website Launched')
            login = LoginPage(self.driver)
            logs.debug('Clicked on register Button')
            login.registerbtnOption().click()
            logs.debug('Gender Selected')
            login.genderInputOption().click()
            logs.debug('Fname Entered')
            login.fnameInputOption().send_keys("Pradeep")
            logs.debug('Lname Entered')
            login.LnameInputOption().send_keys("Mahajan")
            logs.debug('Email Entered')
            login.emailInputOption().send_keys("Mahajan@test.com")

            logs.debug('Password Entered')
            login.passwordInputOption().send_keys("TEst123456789@#$")

            logs.debug('Password re Entered')
            login.confirmpasswordInputOption().send_keys("TEst123456789@#$")

            logs.debug('Register form submitted')
            login.submitbtninputOption().click()

            Checkout = CheckoutPage(self.driver)

            logs.debug('Clicked on Computer tab')
            Checkout.computerTabOption().click()

            logs.debug('Notebook selected')
            Checkout.notebooklinkOption().click()

            logs.debug('Added to cart')
            Checkout.addTocartOption().click()

            logs.debug('Shopping cart opened')
            Checkout.shoppingCarbtnOption().click()

            # logs.debug('Country selected')
            # x = Checkout.countryOption()
            # sel=Select(x)
            # time.sleep(2)
            # sel.select_by_value(41)

            logs.debug('Termsofservice selected')
            Checkout.checktermsofserviceOption().click()

            logs.debug('Clicked on checkout')
            Checkout.checkoutOption().click()



            self.takescreenshot(self.driver)
            logs.debug('Successfully Register')
        except Exception as ex:
            logs.error(f"Exception occurred: {ex}")
            self.takescreenshot(self.driver)