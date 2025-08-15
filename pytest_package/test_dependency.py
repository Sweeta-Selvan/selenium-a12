import pytest
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)
driver.get('https://demowebshop.tricentis.com/')

class TestRegister:
    @pytest.mark.dependency()
    def test_reg(self):
        driver.find_element('xpath', '//a[text() = "Registerrrr"]').click()

    @pytest.mark.dependency(depends =['TestRegister::test_reg'])
    def test_gender(self):
        driver.find_element('xpath', '//input[@id="gender-female"]').click()
    def test_fname(self):
        driver.find_element('xpath', '//input[@name="FirstName"]').send_keys('Mishri')
    def test_lname(self):
       driver.find_element('xpath', '//input[@name="LastName"]').send_keys('Kannan')
    def test_email(self):
        driver.find_element('xpath', '//input[@name="Email"]').send_keys('mishrikannan@gmail.com')


        

