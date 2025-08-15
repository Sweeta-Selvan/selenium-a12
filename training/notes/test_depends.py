import time
import pytest

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# wait_obj = WebDriverWait(driver, 5)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# @pytest.mark.dependency()           ## Independent testcase
# def test_login():
#     driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
#     time.sleep(1)
#     driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
#     time.sleep(1)
#     driver.find_element('xpath', '//input[@id="login-buttonnnn"]').click()
#     time.sleep(2)
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
#
#
# @pytest.mark.dependency(depends=['test_login'])         ## dependent testcase
# def test_logout():
#     driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
#     time.sleep(2)
#     driver.find_element('xpath', '//a[text()="Logout"]').click()


###############################################################################################################

@pytest.mark.dependency()           ## Independent testcase
def test_login():
    print("login executing")

@pytest.mark.dependency(depends=['test_login'])     ## Dependent testcase
def test_logout():
    print("logout executing")

## collected 2 items
## test_depends.py::test_login     login executing         PASSED
## test_depends.py::test_logout    logout executing        PASSED

## Independent testcase is working fine, so dependent testcase also will work fine

###############################################################################################################

@pytest.mark.dependency()                           ## Independent testcase
def test_login():
    prit("login executing")

@pytest.mark.dependency(depends=['test_login'])     ## Dependent testcase
def test_logout():
    print("logout executing")

## collected 2 items
## test_depends.py::test_login     FAILED
## test_depends.py::test_logout    SKIPPED (test_logout depends on test_login)


## Independent is not working fine, so dependent testcase is skipped

###############################################################################################################

@pytest.mark.dependency()           ## Independent testcase
def test_login():
    print("login executing")

@pytest.mark.dependency()           ## Independent testcase
def test_signup():
    print("signup executing")

@pytest.mark.dependency(depends=['test_login', 'test_signup'])     ## Dependent testcase
def test_logout():
    print("logout executing")

## collected 3 items
## test_depends.py::test_login     login executing     PASSED
## test_depends.py::test_signup    signup executing    PASSED
## test_depends.py::test_logout    logout executing    PASSED


###############################################################################################################

@pytest.mark.dependency()           ## Independent testcase
def test_login():
    print("login executing")

@pytest.mark.dependency()           ## Independent testcase
def test_signup():
    pr("signup executing")

@pytest.mark.dependency(depends=['test_login', 'test_signup'])     ## Dependent testcase
def test_logout():
    print("logout executing")

## collected 3 items
## test_depends.py::test_login     login executing     PASSED
## test_depends.py::test_signup                        FAILED
## test_depends.py::test_logout                        SKIPPED (test_logout depends on test_signup)

###############################################################################################################

class TestSample:

    @pytest.mark.dependency()
    def test_login(self):
        print("login executing")

    @pytest.mark.dependency(depends=['test_login'])
    def test_logout(self):
        print("logout executing")

## collected 2 items
## test_depends.py::TestSample::test_login     login executing     PASSED
## test_depends.py::TestSample::test_logout                        SKIPPED (test_logout depends on test_login)


###############################################################################################################

class TestSample:

    @pytest.mark.dependency()
    def test_login(self):
        print("login executing")

    @pytest.mark.dependency(depends=['TestSample::test_login'])
    def test_logout(self):
        print("logout executing")

# ###############################################################################################################
#
class TestSample:

    @pytest.mark.dependency()
    def test_login(self):
        print("login executing")

    @pytest.mark.dependency()
    def test_reg(self):
        print("reg executing")

    @pytest.mark.dependency(depends=['TestSample::test_login', 'TestSample::test_reg'])
    def test_logout(self):
        print("logout executing")

###############################################################################################################

class TestSample:

    @pytest.mark.dependency()
    def test_login(self):
        print("login executing")

    @pytest.mark.dependency()
    def test_reg(self):
        print("reg executing")


class TestSpam:

    @pytest.mark.dependency(depends=['TestSample::test_login', 'TestSample::test_reg'])
    def test_logout(self):
        print("logout executing")


























