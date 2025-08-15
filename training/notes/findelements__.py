import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# # print(footer_elements)          ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5,....wb22]
#
# for ele in footer_elements:
#     print(ele.text)

######################################################################################
## Eg2

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# popular_searches =  driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]//a')
# # print(popular_searches)     ## [wb1, wb2, wb3, wb4, wb5,...wb47]        ## list of web-elements
#
# for element in popular_searches:
#     print(element.text)

######################################################################################
## Eg3

'''
links will be defined for href attribute and href attribute is defined only under the anchor tag
'''

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# all_links = driver.find_elements('tag name', 'a')
# # print(all_links)            ## [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,....]
#
# for link in all_links:
#     print(link.get_attribute('href'))

#############################################################################################################

# ## Eg4
#
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.myntra.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
time.sleep(2)

driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
time.sleep(2)

shoe_data_list = driver.find_elements('xpath', '//div[@class="product-productMetaInfo"]')
# print(shoe_data_list)       ## list of web-elements         ## [wb1, wb2, wb3, wb3,...wb50]

for shoe in shoe_data_list:
    print(shoe.text)
    print("-----------------------------------------------------------------------------")

#############################################################################################################

# ## Alternate solution
#
# from selenium import webdriver

# driver = webdriver.Firefox()

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(2)
#
# driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(2)
#
# shoes_list = []
# shoes_names = driver.find_elements('xpath', '//h4[@class="product-product"]')
# for shoe in shoes_names:
#     shoes_list.append(shoe.text)
#
#
# prices_list = []
# shoes_prices = driver.find_elements('xpath', '//div[@class="product-price"]')
# for shoe in shoes_prices:
#     prices_list.append(shoe.text)
#
#
# for shoe, price in zip(shoes_list, prices_list):
#     print(shoe, '=', price)

##################################################################################################

'''
8.  wap to print all the colors available for adidas shoes in myntra
9.  Go to https://in.bookmyshow.com/, give the location and wap to print all the recommended movies
'''
































