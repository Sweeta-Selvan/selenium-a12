import time

## Eg1
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.instagram.com/')
time.sleep(2)

driver.find_element('name', 'username').send_keys('sherlock_holmes')
time.sleep(1)
driver.find_element('name', 'password').send_keys('sher@12345')

################################################################################

## Eg2
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('name', 'firstname').send_keys('harry')
time.sleep(1)
driver.find_element('name', 'lastname').send_keys('potter')
time.sleep(1)
driver.find_element('name', 'reg_email__').send_keys('harry@gmail.com')
time.sleep(1)
driver.find_element('name', 'reg_passwd__').send_keys('harry@12345')



































































