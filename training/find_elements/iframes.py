import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)
driver.get('https://www.linkedin.com/')
driver.implicitly_wait(30)
gframe = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')
driver.switch_to.frame(gframe)
driver.find_element('xpath', '//span[text() = "Continue with Google"]').click()
driver.switch_to.parent_frame()
