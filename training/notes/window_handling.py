import time

# ## Eg1
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# ac_obj = ActionChains(driver)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# handles = driver.window_handles
# print(handles)          ## list of handles
#
# ## Scrolled down till the end of the application
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## clicking on google+
# driver.find_element('xpath', '//a[text()="Google+"]').click()       ## opens in a new window
# time.sleep(2)
#
# ## Initialize the window handles
# handles2 = driver.window_handles
# print(handles2)         ## list of handles          ## [parent_handle, child_handle]
#
# ## handles2[0]  --> parent_handle
# ## handles2[1]  --> child handle
#
# ## switch the driver from parent to child
# driver.switch_to.window(handles2[1])
#
# ## perform the operations inside the child window
# driver.find_element('xpath', '//input[@title="Search This Blog"]').send_keys('Google pixel')
# time.sleep(2)
#
# ## switch back to the parent window
# driver.switch_to.window(handles2[0])
# time.sleep(2)
#
# ## clicking on youtube
# driver.find_element('xpath', '//a[text()="YouTube"]').click()       ## opens in new window
# time.sleep(2)
#
# ## Initialize window handles
# handles3 = driver.window_handles
# print(handles3)         ## [parent_handle, google_handle, youtube_handle]
#
# ## switch the driver to the youtube window
# driver.switch_to.window(handles3[2])
# time.sleep(2)
#
# ## perform the operations inside the child window
# driver.find_element('xpath', '//input[@name="search_query"]').send_keys('KGF')

#################################################################################################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.implicitly_wait(20)
ac_obj = ActionChains(driver)

driver.get('https://www.firstcry.com/')
time.sleep(4)

driver.find_element('xpath', '//img[@title="rakhi_desktop_def_page_dhotikurtaset"]').click()
time.sleep(2)

handles = driver.window_handles
print(handles)      ## [parent_handle, child_handle]

driver.switch_to.window(handles[1])
time.sleep(2)

driver.find_element('xpath', '//span[text()="See More"]').click()
time.sleep(3)

all_brands = driver.find_elements('xpath', '//ul[@id="brandfltseetop"]//div')
# print(all_brands)       ## list of web-elements

for brand in all_brands:
    print(brand.text)








