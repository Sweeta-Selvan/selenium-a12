# def test_login():
#     print('login executing')
# def test_logout():
#     print('logout excecuting')

#####################nested test fn#####################################
# def test_login():
#     print('login executing')
#     def test_logout():
#         print('logut exceuted')
#############################using fn call################################################
# def test_login():
#     print('login executing')
# def test_logout():
#     print('logut exceuted')
# test_login()
# test_logout()
###############################TestClass##################################################

# class TestSample:
#     def test_login(self):
#         print('login executing')
#     def test_logout(self):
#         print('logout executed')
# test_obj = TestSample()
# test_obj.test_login()
############################################################################################

# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get('https://demowebshop.tricentis.com/')
# class TestRegister:
#     def test_reg(self):
#         driver.find_element('xpath', '//a[text() = "Register"]').click()
#     def test_gender(self):
#         driver.find_element('xpath', '//input[@id="gender-female"]').click()
#     def test_fname(self):
#         driver.find_element('xpath', '//input[@name="FirstName"]').send_keys('Mishri')
#     def test_lname(self):
#         driver.find_element('xpath', '//input[@name="LastName"]').send_keys('Kannan')
#     def test_email(self):
#         driver.find_element('xpath', '//input[@name="Email"]').send_keys('mishrikannan@gmail.com')


      