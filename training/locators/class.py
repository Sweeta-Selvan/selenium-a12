import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)
driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)
driver.find_element ('class name', 'ico-register').click()
time.sleep(1)
driver.find_element('class name','ico-login').click()
time.sleep(1)
driver.find_element('class name','cart-label').click()
time.sleep(1)
driver.close()