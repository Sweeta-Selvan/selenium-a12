'''
The operations which are performed using mouse/keyboard, we call them as low-level operations.
To perform low-level operations in selenium, we go for ActionChains

First we have to import ActionChains
We should import keys for keyboard operations

    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys

    ac_obj = ActionChains(driver)

'''
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)


##################################################################################################################
# ## Mouse hovering operations
# ## Eg1
# driver.get('https://www.swarovski.com/')
# time.sleep(2)
#
# ele1 = driver.find_element('xpath', '//span[text()="Jewelry"]')
# ac_obj.move_to_element(ele1).perform()
# time.sleep(2)
#
# ele2 = driver.find_element('xpath', '//span[text()="Decorations"]')
# ac_obj.move_to_element(ele2).perform()
# time.sleep(2)

##--------------------------------------------------------------------------------------------------------

# ## Eg2
#
# driver.get('https://www.shoppersstop.com/')
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="WOMEN"])[1]')
# watches = driver.find_element('xpath', '(//a[text()="WATCHES"])[1]')
# brands = driver.find_element('xpath', '(//a[text()="BRANDS"])[1]')
#
# ac_obj.move_to_element(women).perform()
# time.sleep(2)
# ac_obj.move_to_element(watches).perform()
# time.sleep(2)
# ac_obj.move_to_element(brands).perform()


###############################################################################################################
#
# ## double click
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele1 = driver.find_element('xpath', '//button[text()="Copy Text"]')
# ac_obj.double_click(ele1).perform()
# time.sleep(2)
#
# ele2 = driver.find_element('xpath', '//label[text()="Name:"]')
# ac_obj.double_click(ele2).perform()

###############################################################################################################

# ## Right click
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# # ac_obj.context_click().perform()
# ## If we dont pass any web-element for the context click, it will right click at the beginning of the application
#
#
## To right click at a specific web-element
# ele = driver.find_element('xpath', '//h2[text()="Dynamic Button"]')
# ac_obj.context_click(ele).perform()

###############################################################################################################

## SCROLLING OPERATIONS

# ## scroll to a particular element
# driver.get('https://www.shoppersstop.com/')
# time.sleep(3)
#
# ele = driver.find_element('xpath', '//h4[text()="Pay securely by"]')
# ac_obj.scroll_to_element(ele).perform()

##--------------------------------------------------------------------------------------

# ## Scroll down to the end of the application
#
# driver.get('https://www.shoppersstop.com/')
# time.sleep(2)
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## To scroll back to the start of the application
# ac_obj.send_keys(Keys.HOME).perform()

# ##------------------------------------------------------------------------------------
# ## Pagedown and pageup operations
#
# driver.get('https://www.shoppersstop.com/')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()

###############################################################################################################

# ## Drag and drop operations
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
#
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()

###############################################################################################################

# ## Tab
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Harry')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.TAB).perform()
# time.sleep(1)
# ac_obj.send_keys('Potter').perform()

###############################################################################################################

# ## Backspace
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Ankitha Shetty')
# time.sleep(2)
# ac_obj.send_keys(Keys.BACKSPACE).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.BACKSPACE).perform()

###############################################################################################################

# ##
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]')
#
# fname = driver.find_element('xpath', '//input[@name="firstname"]')
# lname = driver.find_element('xpath', '//input[@name="lastname"]')
#
#
# fname.send_keys('Ankitha')
#
# fname.send_keys(Keys.CONTROL + 'a')      ## select data present in ele1
# fname.send_keys(Keys.CONTROL + 'c')      ## copy data present in ele1
#
# ## paste it to ele2
# ac_obj.send_keys(Keys.TAB).perform()
# lname.send_keys(Keys.CONTROL + 'v')

###############################################################################################################



























