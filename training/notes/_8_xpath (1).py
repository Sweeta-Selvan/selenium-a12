
# xpath   :   It is a locator used to locate any element on the web-application uniquely.
#             Using xpath, we can locate the web-elements using attributes, can locate text, indexing is possible,
#             can locate dynamically changing elements, can locate any element on the web-application

#             There are 2 types of xpath
#             *   Absolute xpath  :   Starts from the root of html


#             *   Relative xpath  :

'''
import time

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\css_selector_dup.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/input[1]').send_keys('Ram')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/input[2]').send_keys('ram@12345')

#####################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')

#####################################################################################################
## Relative xpath

'''
# attribute name and value    :   //tagname[@attr_name="attr_value"]   

'''

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

###################################################################################################
# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Sakhi')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lastname"]').send_keys('Kadam')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="reg_email__"]').send_keys('sakhi@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="reg_passwd__"]').send_keys('sakhi@12345')

###################################################################################################
# ## Eg3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[@data-group="home"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="women"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="genz"]').click()

###################################################################################################
'''
# text    :   //tagname[text()="text"]   
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Mobiles"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Flights"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Login"]').click()

###################################################################################################
# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.swarovski.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Jewelry"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Accessories"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Swarovski Created Diamonds"]').click()
#
# ###################################################################################################
# ## Eg3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.amazon.in/')
# time.sleep(4)
#
# driver.find_element('xpath', '//a[text()="Bestsellers"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Customer Service"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Amazon Pay"]').click()

###################################################################################################
'''
# Group indexing  :   any_xpath
'''

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Sakhi')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('sakhi@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[3]').send_keys('9876543212')

###################################################################################################
# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@class="inputtext _58mg _5dba _2ph-"])[1]').send_keys('Sakhi')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@class="inputtext _58mg _5dba _2ph-"])[2]').send_keys('Kadam')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@class="inputtext _58mg _5dba _2ph-"])[5]').send_keys('sakhi@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@class="inputtext _58mg _5dba _2ph-"])[7]').send_keys('sakhi@12345')

###################################################################################################
'''
# contains    :   To locate the partial text of any tagname
                # SYNTAX  :   //tagname[contains(text(), "partial_text")]

'''

## Eg1x

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.linkedin.com')
# time.sleep(2)
#
# element = driver.find_element('xpath', '//h2[contains(text(), "Explore collaborative articles")]')
# print(element)

#############################################################################################################

# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.giva.co/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "GIVA Bday Sale")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Card")]').click()


#############################################################################################################

# ## EG3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.kushals.com/')
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Wedding Store")])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Happy Customers")])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Celeb Corner")])[2]').click()

#############################################################################################################

'''
# Dependent-independent xpath
# *   Identify the dependent-independent element
# *   Write the xpath of the independent element
# *   Traverse back until we get the common match for dependent-independent element
# *   Continue writing the xpath of the dependent element
# '''

####################################################################################################
'''
# wap to click on the checkbox of ruby in demo.html
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\demo.html')
# time.sleep(2)
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()


####################################################################################################
'''
# 2.  wap to click on the download link of windows
'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()


####################################################################################################
'''
wap to click on the release notes of python 3.9.22
'''
# from selenium import webdriver

# driver = webdriver.Firefox()

# driver.get('https://www.python.org/')
# time.sleep(2)

# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(3)
# driver.find_element('xpath', '//a[text()="Python 3.9.22"]/../..//a[text()="Release Notes"]').click()



































































