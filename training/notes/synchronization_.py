'''
Synchronization :   Matching the speed of the webdriver to speed of the web-application

There are 2 types of synchronization
*   unconditional synchronization   :   No conditions are passed
            We achieve the unconditional synchronization by passing time.sleep(n)
            Unnecessary wait is too much in unconditional synchronization

*   conditional synchronization     :   Conditions are passed
            There are 2 types
            *   implicit_wait   :   Conditions are internally taken
                    SYNTAX  :   driver.implicitly_wait(n)
                    Here there is no unnecessary wait
                    implicit_wait will make the driver wait until the element is available on the application.
                    As soon as the element is located, it will start performing the operations right  away


            *   explicit_wait   :   Conditions are externally given
                                    Here the wait process will happen based on a condition.

                                    We have import few statement
                                    from selenium.webdriver.support.ui import WebDriverWait
                                    from selenium.webdriver.support import expected_conditions
                                            WebDriverWait --> class
                                            expected_conditions --> module

                                    wait_obj = WebDriverWait(driver, timeouttime)


'''
import time

## Eg1
## unconditional synchronization
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\loading.html')
time.sleep(25)

driver.find_element('xpath', '//input[@name="fname"]').send_keys('Pooja')
time.sleep(1)
driver.find_element('xpath', '//input[@name="lname"]').send_keys('NK')


##############################################################################################################

## Eg1
## implicit_wait
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\loading.html')
driver.implicitly_wait(30)

driver.find_element('xpath', '//input[@name="fname"]').send_keys('Pooja')
time.sleep(1)
driver.find_element('xpath', '//input[@name="lname"]').send_keys('NK')

# ##############################################################################################################

## Eg1
## explicit wait

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 30)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\loading.html')

wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))

driver.find_element('xpath', '//input[@name="fname"]').send_keys('Pooja')
time.sleep(1)
driver.find_element('xpath', '//input[@name="lname"]').send_keys('NK')



##############################################################################################################

## Eg2
## explicit_wait

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

wait_obj = WebDriverWait(driver, 30)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
time.sleep(1)
driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauceeeee')
time.sleep(1)
driver.find_element('xpath', '//input[@id="login-button"]').click()
time.sleep(2)

try:
    wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
    print("Valid credentials, Successfull login")
except:
    print("Invalid credentials, Unsuccessfull login")

# ##############################################################################################################

## Eg2
## unconditional synchronization

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\progressbar.html')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click Me"]').click()
time.sleep(50)
driver.find_element('xpath', '//button[text()="Click Me"]').click()


##############################################################################################################

## Eg3
## explicit_wait

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

wait_obj = WebDriverWait(driver, 50)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\progressbar.html')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click Me"]').click()

wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
time.sleep(1)

driver.find_element('xpath', '//button[text()="Click Me"]').click()



























