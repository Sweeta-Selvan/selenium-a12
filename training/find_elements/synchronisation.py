import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver,30)
# driver.get('https://www.saucedemo.com/')
# try:
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath','//input[@id="user-name"]')))
#     driver.find_element('xpath','//input[@id="user-name"]').send_keys('standard_user')
# except:
#     print('the elements are not launched')

driver.get(r'C:\Users\Rajan Quvae\Desktop\selenium_training\training\notes\progressbar.html')
driver.find_element('xpath','//button[text()="Click Me"]').click()
wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
driver.find_element('xpath','//button[text()="Click Me"]').click()
