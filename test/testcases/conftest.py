import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )

@allure.title("URL Open")
@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        service_obj = Service("D:\\GUI_Automation\\chromedriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.get("https://demowebshop.tricentis.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()