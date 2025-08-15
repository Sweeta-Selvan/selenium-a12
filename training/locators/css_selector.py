# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.instagram.com/')
# time.sleep(2)
# driver.find_element('css selector','input[aria-label="Phone number, username, or email"]').send_keys('Sweeta')
# time.sleep(2)
# driver.find_element('css selector','input[type="password"]').send_keys('12345')
# time.sleep(2)
# driver.close()
#------------------------------Assignment-----------------------------
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# driver.get('https://demowebshop.tricentis.com/')
# driver.find_element('css selector', 'a[class="ico-register"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'input[id="gender-female"]').click()
# driver.find_element('css selector','input[name="FirstName"]').send_keys('Sweeta')
# driver.find_element('css selector','input[id="LastName"]').send_keys('Selvan')
# driver.find_element('css selector', 'input[data-val-required="Email is required."]').send_keys('swee123@gmail.com')
# driver.find_element('css selector','input[data-val-required="Password is required."]').send_keys('123456')
# driver.find_element('css selector', 'input[name="ConfirmPassword"]').send_keys('123456')
# -------------------------------Assignment--------------------------------
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.facebook.com/')
# driver.find_element('css selector','input[placeholder="Email address or phone number"]').send_keys('Sweetas@gmail.com')
# driver.find_element('css selector','input[aria-label="Password"]').send_keys('123456')
# driver.close()