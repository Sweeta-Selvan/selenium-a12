# import pytest

# @pytest.fixture(autouse=True, scope = 'module')
# def greet():
#     print('hello, Welcome ALL')
#     yield
#     print('thank you for shopping')

# class TestShopping:
    
#     def test_shop(self):
#         print('products added')
#     def test_billing(self):
#         print('Billing done')

# class TestCart:
#     def test_cart(self):
#         print('products added to cart')



class TestRegister:
    def test_reg(self, browser):
        browser.find_element('xpath', '//a[text() = "Register"]').click()
    def test_gender(self, browser):
        browser.find_element('xpath', '//input[@id="gender-female"]').click()
    def test_fname(self, browser):
        browser.find_element('xpath', '//input[@name="FirstName"]').send_keys('Mishri')
    def test_lname(self, browser):
        browser.find_element('xpath', '//input[@name="LastName"]').send_keys('Kannan')
    def test_email(self, browser):
        browser.find_element('xpath', '//input[@name="Email"]').send_keys('mishrikannan@gmail.com')






























    