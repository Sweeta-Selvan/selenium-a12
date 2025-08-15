'''
markers :   To group the testcases, we go for markers.
There are 2 types of markers.
    *   inbuilt marker  :
            There are 4 types of inbuilt markers
            *   skip
            *   skipif
            *   parametrize
            *   xfail

    *   custom marker

'''

######################################################################################
import pytest


# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="smoke"        -->     test_signup and test_reg will execute
#
# ##############################################################################################################
#
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"           -->     test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="smoke"            -->     test_signup will execute
# ## pytest test_markers.py -vs -m="regression"       -->     test_reg will execute
#
#
# # ##############################################################################################################
#
# @pytest.mark.smoke
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# @pytest.mark.regression
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
#
# ## pytest test_markers.py -vs -m="smoke"                -->     test_login and test_signup will execute
# ## pytest test_markers.py -vs -m="sanity"               -->     test_signup and test_reg will execute
# ## pytest test_markers.py -vs -m="regression"           -->     test_reg and test_logout will execute
# ## pytest test_markers.py -vs -m="smoke and sanity"     -->     test_signup will execute
# ## pytest test_markers.py -vs -m="smoke and regression" -->     all 4 will be deselected
# ## pytest test_markers.py -vs -m="sanity and regression"-->     test_reg will execute
#
# ## pytest test_markers.py -vs -m="smoke or sanity"      -->     test_login, test_signup and test_reg will execute
# ## pytest test_markers.py -vs -m="smoke or regression"  -->     all 4 will be selected
# ## pytest test_markers.py -vs -m="regression or sanity" -->     test_signup, test_reg and test_logout will execute
#
#
# # ##############################################################################################################
# #
# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login     login executing     PASSED
# ## test_markers.py::TestSample::test_signup    signup executing    PASSED
# ## test_markers.py::TestSample::test_reg       reg executing       PASSED
# ## test_markers.py::TestSample::test_logout    logout executing    PASSED
#
# # ##############################################################################################################
#
# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         print("signup executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.regression
#     def test_logout(self):
#         print("logout executing")
#
#
# # ## pytest test_markers.py -vs -m="smoke"      -->     test_signup will execute
# # ## pytest test_markers.py -vs -m="sanity"     -->     all 4 will execute
# # ## pytest test_markers.py -vs -m="regression" -->     test_logout will execute
#
#
# # ##############################################################################################################
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         print("signup executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.regression
#     def test_logout(self):
#         print("logout executing")

# # ##############################################################################################################

'''
skip    :   To skip the execution of the testcases we go for this marker
            This is an unconditional skip
            To skip the testcase, we dont have to pass any condition or a reason.
            We just have to decorate the testcase with @pytest.mark.skip
            
            SYNTAX  :   @pytest.mark.skip
                        def test_case():
                            pass
'''

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
#
# ## collected 4 items
# ## test_markers.py::test_login     login executing     PASSED
# ## test_markers.py::test_signup                        SKIPPED (unconditional skip)
# ## test_markers.py::test_reg                           SKIPPED (unconditional skip)
# ## test_markers.py::test_logout    logout executing    PASSED
#

###########################################################################################

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip(reason="signup already done")
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip(reason="reg already done")
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login     login executing         PASSED
# ## test_markers.py::test_signup                            SKIPPED (signup already done)
# ## test_markers.py::test_reg                               SKIPPED (reg already done)
# ## test_markers.py::test_logout    logout executing        PASSED


###########################################################################################

# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login     SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup    SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_reg       SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout    SKIPPED (unconditional skip)

###########################################################################################

'''
skipif  :   This is also used to skip the execution of the testcases, but the skip is based on a condition

            SYNTAX  :   @pytest.mark.skipif(condition, reason)
                        def test_case():
                            pass
            
                        condition and reason both are mandatory parameters
                        
                        If the condition is True, it will skip the execution of the testcase
                        If the condition is False, it will execute the testcase
                        
                        If we dont specify the reason, it will give error.
                        If we dont specify the condition, by default the condition will be considered as True and it will skip the execution of the testcase
            
'''

# @pytest.mark.skipif(True, reason='login already done')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login SKIPPED (login already done)

############################################################################################################

# @pytest.mark.skipif(False, reason='login already done')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     login executing     PASSED

############################################################################################################

# @pytest.mark.skipif(False)
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login         ERROR
#
# ## ERROR because reason is not given for skipif
# ## reason is the mandatory parameter


############################################################################################################

# @pytest.mark.skipif(reason='unnnecessary testcase')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     SKIPPED (unnnecessary testcase)
#
# ## If we dont specify the condition, by default it will consider as True and will skip the execution of the testcase

############################################################################################################

'''
xfail   :   This is an expected failure

            SYNTAX  :   @pytest.mark.xfail
                        def test_case():
                            pass 
                    
                        Meaning, we are expecting a failure from the testcase
                        
                        We are expecting a failure and if the test_case fails, then our output will be XFAIL 
                        We are expecting a failure and if the test_case passes, then our output will be XPASS 


'''

import time

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# wait_obj = WebDriverWait(driver, 5)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
#
# @pytest.mark.xfail
# def test_login():
#     driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
#     time.sleep(1)
#     driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
#     time.sleep(1)
#     driver.find_element('xpath', '//input[@id="login-button"]').click()
#     time.sleep(2)
#
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))

######################################################################################

# @pytest.mark.xfail
# def test_login():
#     raise Exception
#
# ## collected 1 item
# ## test_markers.py::test_login XFAIL

######################################################################################
#
# @pytest.mark.xfail
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     login executing         XPASS

############################################################################################################

'''
parametrize markers
'''

@pytest.mark.parametrize('a, b', [(10, 20)])
def test_add(a, b):
    print(a + b)

## collected 1 item
## test_markers.py::test_add[10-20]    30      PASSED

# #############################################################################
#
# @pytest.mark.parametrize('a, b', [(10, 20), (1, 2), (-10, 20), (0, 0), (10, 10)])
# def test_add(a, b):
#     print(a + b)
#
#
# ## collected 5 items
# ## test_markers.py::test_add[10-20]    30      PASSED
# ## test_markers.py::test_add[1-2]      3       PASSED
# ## test_markers.py::test_add[-10-20]   10      PASSED
# ## test_markers.py::test_add[0-0]      0       PASSED
# ## test_markers.py::test_add[10-10]    20      PASSED
#
# #############################################################################
#
# @pytest.mark.parametrize('a, b', [(10, 20, 30)])
# def test_add(a, b):
#     print(a + b)
#
# ## ERROR
#
# #############################################################################
#
# @pytest.mark.parametrize('a, b', [(10, 20)])
# def test_add(a, b, c):
#     print(a + b + c)
#
#
# ## ERROR























































