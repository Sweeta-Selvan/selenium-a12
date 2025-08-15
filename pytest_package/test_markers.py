import pytest
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)
driver.get('https://demowebshop.tricentis.com/')
class TestRegister:
    def test_reg(self):
        driver.find_element('xpath', '//a[text() = "Register"]').click()
    @pytest.mark.skipif(reason= 'already done')
    def test_gender(self):
        driver.find_element('xpath', '//input[@id="gender-female"]').click()
    @pytest.mark.skipif(reason='already done')
    def test_fname(self):
        driver.find_element('xpath', '//input[@name="FirstName"]').send_keys('Mishri')
    def test_lname(self):
        driver.find_element('xpath', '//input[@name="LastName"]').send_keys('Kannan')
    def test_email(self):
        driver.find_element('xpath', '//input[@name="Email"]').send_keys('mishrikannan@gmail.com')

# @pytest.mark.sanity
# def test_login():
#     print('login exceuted')
# def test_sign_up():
#     print('sign up executing')
