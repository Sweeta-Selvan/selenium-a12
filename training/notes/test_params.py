import time
import pytest

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope="class", params=['chrome', 'firefox', 'edge'])
def browser_setup(request):
    parameter = request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome(opts)
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    elif parameter == 'edge':
        driver = webdriver.Edge()

    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()


class TestRegister:

    def test_register(self, browser_setup):     ## browser_setup --> webdriver.Chrome()
        browser_setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender(self, browser_setup):
        browser_setup.find_element('id', 'gender-female').click()

    def test_fname(self, browser_setup):
        browser_setup.find_element('id', 'FirstName').send_keys('Janvi')

    def test_lname(self, browser_setup):
        browser_setup.find_element('id', 'LastName').send_keys('Gopinath')

    def test_reg_email(self, browser_setup):
        browser_setup.find_element('id', 'Email').send_keys('janvi@gmail.com')

    def test_reg_pwd(self, browser_setup):
        browser_setup.find_element('id', 'Password').send_keys('janvi@12345')

    def test_confirm_pwd(self, browser_setup):
        browser_setup.find_element('id', 'ConfirmPassword').send_keys('janvi@12345')


class TestLogin:

    def test_login(self, browser_setup):
        browser_setup.find_element('link text', 'Log in').click()
        time.sleep(1)

    def test_login_email(self, browser_setup):
        browser_setup.find_element('id', 'Email').send_keys('janvi@gmail.com')

    def test_login_pwd(self, browser_setup):
        browser_setup.find_element('id', 'Password').send_keys('janvi@12345')

