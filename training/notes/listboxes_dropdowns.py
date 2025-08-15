'''
A ListBox is a UI element that allows the user to select one or multiple options from a list of items.
If the tagname of the dropdown is "select", then it is a "standard listbox"

There are 2 types
*   single select listbox   :   If we can select only one element from the dropdown, then it is a single select listbox
*   multi select listbox    :   If we can select multiple elements from the dropdown, then it is a multi select listbox

We will handle single-select and multi-select listboxes in the same way

    from selenium.webdriver.support.select import Select
    select_obj = Select(listbox_having_select_tag)

    We have 3 attributes to select the elements from the dropdown
    *   select_by_index     :   Will select the element from the dropdown by passing the index number
                                SYNTAX  :   select_obj.select_by_index(index_num)

    *   select_by_value     :   Will select the element from the dropdown by passing the value of the value attribute
                                SYNTAX  :   select_obj.select_by_value("value")

    *   select_by_visible_text  :   Will select the element from the dropdown by passing the text
                                SYNTAX  :   select_obj.select_by_visible_text("text")


    We have 3 attributes to deselect the elements from the dropdown
    *   deselect_by_index     :   Will deselect the element which is present in that index number
                                SYNTAX  :   select_obj.deselect_by_index(index_num)

    *   deselect_by_value     :   Will deselect the element of the value passed
                                SYNTAX  :   select_obj.deselect_by_value("value")

    *   deselect_by_visible_text  :   Will deselect the element having the given text
                                SYNTAX  :   select_obj.deselect_by_visible_text("text")


    *   select_obj.deselect_all()   :   This will deselect all the selected elements
'''

import time

'''
1.  program to select the month in https://www.facebook.com/r.php?entry_point=login using Select class attributes
'''

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# month = driver.find_element('xpath', '//select[@id="month"]')
# select_obj = Select(month)
#
# #--------------------------------------------------------------------------------------
# ## select_by_index
# select_obj.select_by_index(3)
# time.sleep(2)
# select_obj.select_by_index(10)
# time.sleep(2)
# select_obj.select_by_index(1)
# time.sleep(2)
#
# select_obj.select_by_index(100)     ## NoSuchElementException: Message: Could not locate element with index 100
#
# # NOTE :   When we give the index number out of range, it will give NoSuchElementException
#
# ##------------------------------------------------------------------------------------------------
#
# ## select_by_value
# select_obj.select_by_value('12')
# time.sleep(2)
# select_obj.select_by_value('9')
# time.sleep(2)
# select_obj.select_by_value('5')
# time.sleep(2)
# select_obj.select_by_value('8')
#
# ##------------------------------------------------------------------------------------------------
#
# ## select_by_visible_text
# select_obj.select_by_visible_text('Jan')
# time.sleep(2)
# select_obj.select_by_visible_text('Apr')
# time.sleep(2)
# select_obj.select_by_visible_text('Oct')

########################################################################################################

'''
Single select listbox
'''
#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\demo.html')
# time.sleep(2)
#
# listbox = driver.find_element('xpath', '//select[@id="standard_cars"]')
# select_obj = Select(listbox)

# ## select_by_index
# select_obj.select_by_index(5)
# time.sleep(2)
# select_obj.select_by_index(2)
# time.sleep(2)
# select_obj.select_by_index(8)


# ## select_by_value
# select_obj.select_by_value('toy')
# time.sleep(2)
# select_obj.select_by_value('lr')
# time.sleep(2)
# select_obj.select_by_value('hda')


# ## select_by_visible_text
# select_obj.select_by_visible_text('Audi')
# time.sleep(2)
# select_obj.select_by_visible_text('Jaguar')
# time.sleep(2)
# select_obj.select_by_visible_text('Nissan')

#########################################################################################################

'''
Multi select listbox
'''

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\demo.html')
# time.sleep(2)
#
# multi_listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj = Select(multi_listbox)

# ## select_by_index
# select_obj.select_by_index(2)
# time.sleep(2)
# select_obj.select_by_index(4)
# time.sleep(2)
# select_obj.select_by_index(6)

# ## select_by_value
# select_obj.select_by_value('merc')
# time.sleep(2)
# select_obj.select_by_value('bmw')
# time.sleep(2)
# select_obj.select_by_value('toy')

# ## select_by_visible_text
# select_obj.select_by_visible_text('Honda')
# time.sleep(2)
# select_obj.select_by_visible_text('Jaguar')
# time.sleep(2)
# select_obj.select_by_visible_text('Land Rover')

############################################

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\demo.html')
# time.sleep(2)
#
# multi_listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj = Select(multi_listbox)

##---------------------------------------------------------------------------------
# ## select_by_index
# select_obj.select_by_index(2)
# time.sleep(2)
# select_obj.select_by_index(4)
# time.sleep(2)
# select_obj.select_by_index(6)
# time.sleep(2)
#
# ## to deselect the elements
# select_obj.deselect_by_index(4)

##---------------------------------------------------------------------------------

# ## select_by_value
# select_obj.select_by_value('merc')
# time.sleep(2)
# select_obj.select_by_value('bmw')
# time.sleep(2)
# select_obj.select_by_value('toy')
# time.sleep(2)
#
# select_obj.deselect_by_value('merc')

##---------------------------------------------------------------------------------

# ## select_by_visible_text
# select_obj.select_by_visible_text('Honda')
# time.sleep(2)
# select_obj.select_by_visible_text('Jaguar')
# time.sleep(2)
# select_obj.select_by_visible_text('Land Rover')
# time.sleep(2)
#
# # select_obj.deselect_by_visible_text('Jaguar')
#
# ## to deselect all
# select_obj.deselect_all()

#########################################################################################################

'''
Normal listbox
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
# time.sleep(2)
#
# driver.find_element('xpath', '(//div[@role="button"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Vistadome Non AC (VS)"]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//div[@role="button"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="PREMIUM TATKAL"]').click()


#########################################################################################################
# ## ANALYZE THE BELOW CODE
#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E16-May20\files_\demo.html')
# time.sleep(2)
#
# listbox = driver.find_element('xpath', '//select[@id="standard_cars"]')
# select_obj = Select(listbox)
#
# all_cars = driver.find_elements('xpath', '//select[@id="standard_cars"]/option')
# print(all_cars)     ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5,..]
#
# ## select_by_index
# for i in range(0, len(all_cars)):
#     select_obj.select_by_index(i)
#     time.sleep(0.75)

# ## select_by_index  (select only at particular index numbers)
# for i in range(0, len(all_cars)):
#     if i in [2, 5, 8]:
#         select_obj.select_by_index(i)
#         time.sleep(0.75)

#-------------------------------------------------------------------------------

# ## select_by_value
#
# for car in all_cars:        ## for car in [wb1, wb2, wb3, wb4, wb5...wb12]
#     value = car.get_attribute('value')
#     select_obj.select_by_value(value)
#     time.sleep(0.75)

#-------------------------------------------------------------------------------

# ## select_by_visible_text
# for car in all_cars:
#     select_obj.select_by_visible_text(car.text)
#     time.sleep(0.75)































