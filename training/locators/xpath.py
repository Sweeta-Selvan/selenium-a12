# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.saucedemo.com/')
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('sweeta')
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('sweeta@123')

#for meesho search bar=html/body/div/div[2]/div[1]/div/div[2]/div
#-----------------------------relative xpath-----------------------------------------

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('xpath','//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath','//input[@id="password"]').send_keys('secret_sauce')
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# driver.close()
# driver.get('https://www.facebook.com/')
# driver.find_element('xpath','//input[@name="email"]').send_keys('abc123')
# driver.find_element('xpath','//input[@type="password"]').send_keys('1234')

# driver.get('https://www.amazon.com/')
# driver.find_element('xpath','//img[@alt="Dining"]').click()
# driver.find_element('xpath','//i[@class="hm-icon nav-sprite"]').click()

# driver.get('https://www.swarovski.com/en-IN/')
# # driver.find_element('xpath','//span[@aria-label="burger-mobile image"]').click()
# time.sleep(4)
# driver.maximize_window()
# time.sleep(3)
# driver.find_element('xpath','//span[text()="Decorations"]').click()
# time.sleep(2)
# driver.find_element('xpath','//span[text()= "Gifts"]').click()
# time.sleep(2)
# driver.find_element('xpath','//span[text()= "Jewelry"]').click()

# driver.get('https://www.facebook.com/reg/')
# driver.find_element('xpath','//input[@name="firstname"]').send_keys('mishri')
# driver.find_element('xpath','//input[@name="lastname"]').send_keys('rashika')
# driver.find_element('xpath','(//input[@class="inputtext _58mg _5dba _2ph-"])[5]').send_keys('mishri@gmail.com')
# driver.find_element('xpath','(//input[@class="inputtext _58mg _5dba _2ph-"])[7]').send_keys('948583676')
# import time
# from selenium import webdriver
# # opts=webdriver.FirefoxOptions()
# # opts.add_experimental_option('detach',True)
# driver=webdriver.Firefox()

# driver.get('https://www.python.org/')
# driver.find_element('xpath','//a[text()="Downloads"]').click()
# time.sleep(2)
# driver.find_element('xpath','//a[text()="Python 3.13.4"]/../..//a[text()="Release Notes"]').click()

# driver.get('https://www.thehindu.com/')
# time.sleep(2)
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('partial link text','Opinion').click()
# time.sleep(2)
# driver.find_element('xpath','(//a[contains(text(),"Editorial")])[2]').click()
# time.sleep(4)
# driver.find_element('xpath','//strong[contains(text(),"On Tamil Nadu and the fireworks industry blasts")]').click()

# driver.get('https://www.tradingview.com/')
# driver.find_element('xpath','//span[text()="Search"]').click()
# driver.find_element('xpath','//input[@inputmode="search"]').send_keys('silver')

#####################################eg:nestasia#############################################################
# driver.get('https://nestasia.in/')
# time.sleep(2)
# driver.find_element('xpath','//span[text()="New In"]').click()
# time.sleep(6)
# driver.find_element('xpath', '//h3[contains(text(),"Mandala Melange Long Platter Dish Orange")]').click()
# time.sleep(6)
# cutlery_price=driver.find_element('xpath','//h1[contains(text(),"Mandala Melange Long Platter Dish Orange")]/..//div[@class="product-price"]')
# print(cutlery_price.text)
# driver.find_element('xpath','//div[@class="hambergerIcon"]').click()
# time.sleep(1)
#######################################eg:tradingviews#############################################################
# driver.get('https://www.tradingview.com/')
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath','//input[@type="search"]').send_keys('silver')
# time.sleep(1)
# driver.find_element('xpath','//button[@class="searchButton-KLRTYDjH button-KLRTYDjH iconedButton-KLRTYDjH hoveredButton-KLRTYDjH"]').click()
# time.sleep(1)
# silver_price=driver.find_element('xpath','(//span[text()="SILVER"])[2]/../../..//span[text()="36.849"]')
# print(silver_price.text)

# driver.get('https://www.redbus.in/')
# time.sleep(2)
# driver.find_element('xpath','//i[@class="icon___9beafd icon icon-date_range"]').click()

# driver.get('https://nestasia.in/')
# time.sleep(2)
# all_links = driver.find_elements('tag name','a')
# for link in all_links:
#     print(link.get_attribute('href'))