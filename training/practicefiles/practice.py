# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# driver.get('https://www.goibibo.com/bus/')
# time.sleep(2)
# # driver.find_element('xpath', '//input[@placeholder="Pick a date"]').click()
# # time.sleep(3)
# driver.find_element('xpath','//input[@placeholder="Enter Source"]').send_keys('Chennai')
# time.sleep(5)
# driver.find_element('xpath', '//span[text()="Chennai, Tamil Nadu"]').click()
# driver.find_element('xpath','//input[@placeholder="Enter Destination"]').send_keys('Bangalore')
# time.sleep(4)

# # def book(month,date):
# while True:
#     try:
#         driver.find_element ('xpath','//p[text()="December 2025"]/../../..//span[text()="27"]').click()
#         break
#     except:
#         driver.find_element('xpath','(//div[@class="dcalendarstyles__SliderArrow-sc-r2jz2t-14 ilBEvY"])[2]').click()
#########################################dependent and independent xpath#####################################
# driver.get('https://www.swiggy.com/instamart')
# time.sleep(15)
# driver.find_element('xpath', '//div[@class="_3VnBa"]').click()
# time.sleep(1)
# act_obj = driver



# driver.find_element('xpath' '//div[text()="Chips and Namkeens"]').click()
# time.sleep(2)
# driver.find_elements('xpath', '')
##################################################################
# driver.get('https://www.swiggy.com/instamart')
# time.sleep(6)
# # driver.find_element('xpath', '//div[@data-testid="dismiss-button"]').click()
# # time.sleep(5)
# driver.find_element('xpath', '//div[text()="Masalas"]').click()
# time.sleep(5)
# masalas_ = driver.find_elements('xpath', '//div[@class="_2zSij"]')
# for item in masalas_:
#     print(item.text)
###########################################################################
# driver.get('https://www.swiggy.com/instamart')
# time.sleep(15)
# driver.find_element('xpath' , '//div[@class="_3VnBa"]').click()
# time.sleep(4)
# driver.find_element('xpath', '//div[text() = "Masalas"]').click()
# time.sleep(3)
# masalas_ = driver.find_elements('xpath', '//div[@class="_2zSij"]')
# for item in masalas_:
#     print(item.text)

####################################################################################
# import time
# from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get('https://www.ikea.com/in/en/')
# time.sleep(4)
# driver.find_element('xpath','//span[text() = "Home Decor"]' ).click()
# time.sleep(2)
# ikeas = driver.find_elements('xpath' , '//ul[@class="hnf-dropdown__columns"]//a')
# for item in ikeas:
#     print(item.text)
#################################to print the colors in myntra##########################################################
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(2)
# driver.find_element('xpath', '//li[text() = "Adidas Originals Shoes"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//span[text() = "+ "]').click()
# time.sleep(1)
# colors = driver.find_elements('xpath', '//li[@class="colour-listItem"]')
# for item in colors:
#     print(item.text)
# time.sleep(5)
# alert_obj = driver.switch_to.alert

# alert_obj.accept()
# time.sleep(2)
##############################################################################################
# driver.get('https://www.pepperfry.com/')
# time.sleep(3)
# driver.find_element('xpath', '//a[@class="close-modal"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//a[text() = " Kitchen & Dining "]').click()
# time.sleep(1)
# driver.find_element('xpath', '//a[contains(text(), "Ser")]').click()
# time.sleep(1)
# serve_ware = driver.find_elements('xpath', '//div[@class="product-card-bottom padding-8"]')
# for items in serve_ware:
#     print(items.text)

# serve_ware = driver.find_elements('xpath', '//div[@class="product-details marginBottom-4"]')
# for item in serve_ware:
#     print(item.text)
#############################################################################################################3
# driver.get('https://blinkit.com/')
# time.sleep(3)
# # driver.find_element('xpath', '//div[@class="DownloadAppModal__BackButtonIcon-sc-1wef47t-14 hEjBTn"]').click()
# # time.sleep(2)
# driver.find_element('xpath', '//div[text() = "Dairy & Breakfast"]').click()
# time.sleep(1)
# products= driver.find_elements('xpath','class="tw-mb-1.5"')
# for item in products:
#     print(item.text)
######################################################################################################################
# driver.get('')
# time.sleep(2)
# driver.find_element('xpath','//span[text() = "WOMEN"]').click()
########################################################################################################################
# driver.get('https://www.firstcry.com/')
# time.sleep(4)
# driver.find_element('xpath', '//img[@title="rakhi_desktop_def_page_kurtisalwarset"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//div[text()="See More"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//img[@title="rakhi_desktop_def_page_dhotikurtaset"]').click()
# time.sleep(4)
# driver.find_element('xpath','//span[text()="See More"]').click()
# time.sleep(4)
# price = driver.find_elements('xpath', '//div[@class="fsBrandMore seem brd_btm"]')
# for item in price:
#     print(item.text)
############################################################################################################################
# driver.get('https://www.amazon.com/')
# time.sleep(4)
# driver.find_element('xpath','//input[@role="searchbox"]').send_keys('kurta')
# time.sleep(1)
# driver.find_element('xpath','//div[@aria-label="kurta set for women"]').click()
# time.sleep(2)
# driver.find_element('xpath','(//span[text()="See more"])[1]').click()
##############################################################################################################################
# driver.get('https://www.ikea.com/in/en/')
# time.sleep(4)
# driver.maximize_window()
# time.sleep(3)
# driver.find_element('xpath', '//span[text()="Beds & mattresses"]').click()
# time.sleep(1)
# driver.find_element('xpath','//a[text()="Beds"]').click()
# time.sleep(4)
# driver.find_element('xpath','//span[text()="Double beds"]').click()
# time.sleep(4)
# driver.find_element('xpath','//span[text()="Material"]/..').click()
# time.sleep(1)
# driver.find_element('xpath','//span[@class="plp-checkbox--subtle plp-checkbox"]').click()
# time.sleep(1)
# driver.find_element('xpath','(//span[@class="plp-checkbox--subtle plp-checkbox"])[2]').click()
# time.sleep(1)
# driver.find_element('xpath','(//span[@class="plp-checkbox--subtle plp-checkbox"])[3]').click()
#######################################################################################################################
# driver.get('https://www.amazon.com/')
# time.sleep(5)
# driver.find_element('xpath','//input[@type="text"]').send_keys('shirts')
# time.sleep(5)
# driver.find_element('xpath','//div[@aria-label="shirts for women"]').click()
# time.sleep(4)
# driver.find_element('xpath','(//span[text()="Men"])[1]/../../../..//i[@class="a-icon a-icon-checkbox"]').click()
##########################################################################################################################
# driver.get('https://www.myntra.com/')
# time.sleep(4)
# driver.find_element('xpath','//input[@placeholder="Search for products, brands and more"]').send_keys('adidas')
# time.sleep(2)
# driver.find_element('xpath','//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(4)
# driver.find_element('xpath','//div[@class="sort-sortBy"]').click()
# time.sleep(1)
# driver.find_element('xpath','//input[@value="price_desc"]').click()
# driver.find_element('xpath','(//span[@class="atsa-downArrow sprites-arrowDownBold myntraweb-sprite"])[3]').click()
# time.sleep(2)
# driver.find_element('xpath','')
###########################################################################################################################
# driver.get('https://thenmozhidesigns.com/collections/all-salwars')
# driver.implicitly_wait(20)
# driver.find_element('xpath','//span[text()="Sort by"]').click()
# driver.find_element('xpath', '//button[text()="Filter "]').click()
#driver.find_element('xpath', '(//div[@class="accordion-list"])[1]//span[text()="Availability"]').click()
#driver.find_element('xpath', '(//span[text()="Type"])[1]').click()
# driver.find_element('xpath', '(//div[@class="checkbox-control"]//label[text()="Casual Wear"])[2]').click()
############################################################################################################################
# driver.get('https://www.ikea.com/in/en/cat/plates-18861/')
# driver.implicitly_wait(10)
# driver.maximize_window()

# driver.find_element('xpath','//span[text()="Series"]/..').click()
# driver.find_element('xpath','//span[text()="GLADELIG series"]/../../..//span[@class="plp-checkbox--subtle plp-checkbox"]').click()
###########################################################################################################################
# driver.get('https://www.thebodyshop.in/hair/h/c00061')
# driver.implicitly_wait(20)
# driver.maximize_window()
# time.sleep(4)
#################driver.find_element('xpath', '//div[@class="c304"]').click()
#driver.find_element('xpath', '//img[@alt="downArrow"]').click()
#driver.find_element('xpath', '//p[text()="Popular"]').click()###
##################################################################################################
# driver.get('https://www.homecentre.in/in/en/c/furnishing-cushions')
# driver.implicitly_wait(20)
# driver.find_element('xpath', '//span[@class="jss1294"]').click()
###################################################################################################
# driver.get('https://www.minisoindia.com/category/top-categories/bags-and-accessories/')
# driver.implicitly_wait(10)
# driver.find_element('xpath', '//li[@class="active"]//i').click()
######################################################################################################
# driver.get('https://www.myntra.com/adidas-originals-shoes?extra_search_param=isautosuggestentry%3atrue%3a%3aid%3a2297-adidas-originals-shoes&rawQuery=Adidas%20Originals%20Shoes')
# driver.implicitly_wait(10)
# driver.find_element('xpath', '//input[@value="Casual Shoes"]/..').click()
# driver.find_element('xpath', '(//label[contains(@class,"gender-label")])[1]').click()
#########################################################################################################
# driver.get('https://www.croma.com/campaign/deals-on-juicer-mixer-grinder/c/7012?q=%3Arelevance%3Adelivery_mode%3AHome+Delivery')
# driver.implicitly_wait(15)
# driver.maximize_window()
# driver.find_element('xpath', '(//p[text()="Categories"]/../..//span[@class="MuiIconButton-label"])').click()
# driver.find_element('xpath', '(//p[text()="Brand"]/../..//span[@class="MuiIconButton-label"])').click()
# driver.find_element('xpath', '//label[@for="SG-ManufacturerDetails-Brand-Philips"]/span[@class="check"]').click()
# driver.find_element('xpath', '//label[@for="SG-ManufacturerDetails-Brand-Croma"]/span[@class="check"]').click()
# driver.find_element('xpath', '//div[@class="all-filters"]/span').click()
###########################################window_handling_##############################
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach' , True)
# driver= webdriver.Chrome(opts)
# driver.implicitly_wait(20)
# opts.add_argument('--disable_notifications')

# ac_obj = ActionChains(driver)
####################################### Eg1 ####################################################
# driver.get('https://www.makemytrip.com/hotels/')
# driver.implicitly_wait(20)
# ele = driver.find_element('xpath', '//p[text()="Flagship Hotel Stores on MakeMyTrip"]')
# ac_obj.scroll_to_element(ele).perform()
# driver.find_element('xpath', '//div[@class="itemDesc"]/../..//a[text()="BOOK NOW"]').click()
# handles1 = driver.window_handles
# print(handles1)
# driver.switch_to.window(handles1[1])
# scr = driver.find_element('xpath', '//h2[@class="sectionTitle textCenter appendTop70"]')
# ac_obj.scroll_to_element(scr).perform()
########################################### Eg 2 ###################################################
# driver.get('https://www.firstcry.com/')
# driver.implicitly_wait(20)
# driver.maximize_window()
# ele = driver.find_element('xpath', '//img[@alt="rakhi_desktop_def_page_babyessentials"]')
# ac_obj.scroll_to_element(ele).perform()
# ac_obj.send_keys(Keys.END).perform()
######################################## eg 3 #########################################################
# driver.get('https://www.naukri.com/')
# driver.implicitly_wait(20)
# driver.find_element('xpath', '//div[text() = "Services"]').click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# ele = driver.find_element('xpath', '//div[text()="See Samples"]')
# ac_obj.scroll_to_element(ele).perform()
# driver.find_element('xpath', '(//input[@name="name"])[2]').send_keys('Mishri')
# driver.find_element('xpath', '(//input[@name="email"])[2]').send_keys('mishri123@gmail.com')
# driver.switch_to.window(handles[0])
# driver.find_element('xpath', '//div[text() = "Companies"]').click()
#######################################################################################################
# driver.get('https://www.theindusvalley.in/collections/tri-ply-stainless-steel?filter.v.price.gte=&filter.v.price.lte=&sort_by=manual')
# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.find_element('xpath', '(//span[@class="collection-filterarrow flexbox align-center justify-center"])[3]').click()
# driver.find_element('xpath', '//input[@value="Casserole/Biriyani Pot/stockpot"]').click()
# ele = driver.find_element('xpath', '(//a[contains(text(), "TurboCuk Tri-ply Stainless Steel Cookware Set:")])[2]')
# ac_obj.scroll_to_element(ele).perform()
# driver.find_element('xpath', '(//span[@class="collection-filterarrow flexbox align-center justify-center"])[2]').click()
#########################################################################################################
# driver.get('https://www.myntra.com/')
# driver.implicitly_wait(20)

# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
# driver.find_element('xpath','//li[text()="Adidas Bags"]').click()
    
# driver.find_element('xpath', '//label[text() = "Backpacks"]').click()
    
# ele = driver.find_element('xpath', '//span[@class="myntraweb-sprite sort-downArrow sprites-downArrow"]')
# ac_obj.move_to_element(ele).perform()
    
# driver.find_element('xpath', '//label[contains(text(), "Popularity")]').click()
###############################################ASSIGNMENT QNO 1 ####################################################
from selenium import webdriver
from selenium.webdriver.support.select import Select
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)

driver. get('https://www.globalsqa.com/demo-site/select-dropdown-menu/')
driver.implicitly_wait(20)
# driver.find_element('xpath', '//div[@id="dismiss-button"]').click()

ele = driver.find_element('tag name', 'select' )

select_obj = Select(ele)
select_obj.select_by_value('ALB')
select_obj.select_by_index(12)
select_obj.select_by_index(14)
select_obj.select_by_index(8)
select_obj.select_by_index(34)
###################################################ASSIGNMENT QNO 2#################################################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 30)

driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
driver.find_element('xpath','//button[text()= "Start"]').click()
ele = wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//h4[text() = "Hello World!"]')))
print(ele.text)
###############################################ASSIGNMENT QNO 3######################################################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
driver = webdriver.Firefox() 
# opts.add_argument('--disable-notifications')
wait_obj = WebDriverWait(driver,30)
driver.implicitly_wait(20)
driver.get('https://www.saucedemo.com/')
driver.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
driver.find_element('xpath', '//input[@type="password"]').send_keys('secret_sauce')
driver.find_element('xpath', '//input[@id="login-button"]').click()
driver.find_element('xpath', '//div[text() = "Sauce Labs Backpack"]/../../..//button[@data-test="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element('xpath', '//div[text()= "Sauce Labs Bike Light"]/../../..//button[@name="add-to-cart-sauce-labs-bike-light"]').click()
driver.find_element('xpath', '//a[@class="shopping_cart_link"]').click()
ele1 = wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="Sauce Labs Backpack"]')))
ele2 = wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="Sauce Labs Bike Light"]')))
if ele1 and ele2:
    print('products ----------added -----------to cart and its verified ')
driver.find_element('xpath', '//button[@data-test="checkout"]').click()
driver.find_element('xpath', '//input[@data-test="firstName"]').send_keys('mishri')
driver.find_element('xpath', '//input[@data-test="lastName"]').send_keys('Kannan')
driver.find_element('xpath', '//input[@data-test="postalCode"]').send_keys('346576')
driver.find_element('xpath', '//input[@data-test="continue"]').click()
driver.find_element('xpath', '//button[@id="finish"]').click()
driver.find_element('xpath', '//button[@name="back-to-products"]').click()
