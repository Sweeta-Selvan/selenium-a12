'''
class name  :   If we are having "class" attribute, then we can go for "class name" locator
                *   class is not unique.
                    Incase of multiple occurances, class name will always consider the first occurance
                *   class name locator cannot locate the spaces.
                    SO whenever we have space the value of the class attribute, we replace the space with dot(.)

'''
import time

## Eg1
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('class name', 'ico-register').click()
time.sleep(2)
driver.find_element('class name', 'ico-login').click()
time.sleep(2)
driver.find_element('class name', 'ico-cart').click()

##############################################################################################
# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\css_selector.html')
# time.sleep(2)
# driver.find_element('class name', 'first_row').send_keys('Jack')
# time.sleep(1)
# driver.find_element('class name', 'first_row').send_keys('Jill')
#
# ## Both the values will be filled in the first occurance

##############################################################################################
## Eg3

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('class name', 'input_error form_input').send_keys('standard_user')
#
# ## NoSuchElementException
# ## Because class name locator cannot locate the spaces.

##------------------------------------------------------------------------------

## To overcome this drawback, we should replace the space with dot(.)

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('class name', 'input_error.form_input').send_keys('standard_user')































