import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from mainfolder.objects.CheckoutPage import *
from mainfolder.objects.LoginPage import LoginPage
from mainfolder.objects.RegisterPage import RegisterPage
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
            register = RegisterPage(self.driver)
            logs.debug('Clicked on register Button')
            register.registerbtnOption().click()
            logs.debug('Gender Selected')
            register.genderInputOption().click()
            logs.debug('Fname Entered')
            register.fnameInputOption().send_keys("Pradeep")
            logs.debug('Lname Entered')
            register.LnameInputOption().send_keys("Mahajan")
            logs.debug('Email Entered')
            register.emailInputOption().send_keys("Mahajan123@test.com")

            logs.debug('Password Entered')
            register.passwordInputOption().send_keys("TEst123456789@#$")

            logs.debug('Password re Entered')
            register.confirmpasswordInputOption().send_keys("TEst123456789@#$")

            logs.debug('Register form submitted')
            register.submitbtninputOption().click()

            login = LoginPage(self.driver)

            logs.debug('Click on Login')
            login.loginbtnOption().click()

            logs.debug('username Entered')
            login.usernameInputOption().send_keys("Mahajan123@test.com")

            logs.debug('password Entered')
            login.passwordInputOption().send_keys("TEst123456789@#$")

            logs.debug('Clicked on Login')
            login.log_in_btnOption().click()

            Checkout = CheckoutPage(self.driver)

            logs.debug('Clicked on Computer tab')
            Checkout.computerTabOption().click()

            logs.debug('Notebook selected')
            Checkout.notebooklinkOption().click()

            logs.debug('Added to cart')
            Checkout.addTocartOption().click()

            logs.debug('Shopping cart opened')
            time.sleep(4)
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

            logs.debug('Fname entered')
            Checkout.billingfnameOption().send_keys("Pradeep")

            logs.debug('Lname entered')
            Checkout.billinglnameOption().send_keys("Mahajan")

            logs.debug('Email entered')
            Checkout.billingEmailOption().clear()
            Checkout.billingEmailOption().send_keys("Mahajan@test.com")

            logs.debug('Billing company entered')
            Checkout.billingcompOption().send_keys("Testing")

            logs.debug('Billing Country entered')
            Checkout.billingcountrypOption().send_keys("India")

            logs.debug('Billing City entered')
            Checkout.billingcityOption().send_keys("Indore")

            logs.debug('Billing Add entered')
            Checkout.billingadd1Option().send_keys("Dewas Naka Indore")

            logs.debug('Billing Zip entered')
            Checkout.billingZipOption().send_keys("450331")

            logs.debug('Billing Phone entered')
            Checkout.billingPhoneOption().send_keys("7894561239")

            logs.debug('continue2btn clicked')
            Checkout.continue2btnOption().click()

            logs.debug('continue3btn clicked')
            Checkout.continue3btnOption().click()

            logs.debug('continue4btn clicked')
            Checkout.continue4btnOption().click()

            logs.debug('continue5btn clicked')
            Checkout.continue5btnOption().click()

            logs.debug('Confirm clicked')
            Checkout.confirmbtnOption().click()

            self.takescreenshot(self.driver)
            logs.debug('Order Placed')

        except Exception as ex:
            logs.error(f"Exception occurred: {ex}")
            self.takescreenshot(self.driver)