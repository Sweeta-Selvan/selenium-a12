import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)
ac_obj = ActionChains(driver)
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# handles=driver.window_handles
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Google+"]').click()
# handles1=driver.window_handles
# driver.switch_to.window(handles1[1])
# time.sleep(2)
# driver.find_element('xpath','//input[@type="email"]').send_keys('abc132@gmail.com')
# driver.switch_to.window(handles1[0])
# driver.find_element('xpath','//a[text()="Facebook"]').click()
################################################eg1##################################################################
# driver.get('https://www.firstcry.com/')
# time.sleep(4)
# driver.find_element('xpath', '//img[@title="rakhi_desktop_def_page_dhotikurtaset"]').click()
# time.sleep(4)
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# driver.find_element('xpath','//span[text()="See More"]').click()
# time.sleep(4)
