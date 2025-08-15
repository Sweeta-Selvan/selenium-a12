import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)
# # driver.get('https://nestasia.in/')
# # time.sleep(2)
# # all_links = driver.find_elements('tag name','a')
# # for link in all_links:
# #     print(link.get_attribute('href'))
####################################product name and price##################################
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@placeholder="Search for products, brands and more"]').send_keys('adidas')
# time.sleep(1)
# driver.find_element('xpath','//li[text()="Adidas Originals"]').click()
# time.sleep(1)
# adidas_price = driver.find_elements('xpath', '//div[@class="product-productMetaInfo"]')
# for items in adidas_price:
#     print(items.text)
##########################to print the footers############################
##eg1##
# driver.get('https://nestasia.in/')
# time.sleep(2)
# footer_elements = driver.find_elements('xpath', '(//div[@class="container clearfix"])[3]//li')

# for item in footer_elements:
#     print(item.text)

################################eg2######################################
# driver.get('https://www.ikea.com/in/en/')
# time.sleep(2)
# footer_elements = driver.find_elements('xpath', '//div[@class="hnf-footer__linkGroups"]//a')
# for item in footer_elements:
#     print(item.text)

######################################eg3#########################################
# driver.get('https://www.redbus.in/')
# time.sleep(3)
# footer_elements = driver.find_elements('xpath', '//div[@class="footerContent"]//a')
# for item in footer_elements:
#     print(item.text)
##################################eg4##################################################
# driver.get('https://www.pepperfry.com/?srsltid=AfmBOor_B8vTVorbbDlIeiHyl7ipD-y8AlV-hiyede5n8pVe2OT_DSkr')
# time.sleep(4)
# footer_elements = driver.find_elements('xpath', '//div[@class="row paddingTop-42"]//div')
# for item in footer_elements:
#     print(item.text)