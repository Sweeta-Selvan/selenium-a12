# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.facebook.com/campaign/landing.php?')
# time.sleep(2)
# day_ = driver.find_element('xpath','//select[@aria-label="Day"]')
# select_obj = Select(day_)
# select_obj.select_by_value("3")