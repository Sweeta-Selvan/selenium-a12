'''

iframe  :   The application present inside another application, we call it as iframe

*   Locate the frame1
*   Switch the driver to frame1
    driver.switch_to.frame(frame1)
*   perform operations in frame1
*   If there is another frame inside frame1,
    from frame1 only, we should switch the driver control to the inner_frame
    driver.switch_to.frame(inner_frame)
*   To get back to the child1 frame
    driver.switch_to.frame(frame1)
*   driver.switch_to.parent_frame() --> Will switch to the main application.

'''

import time


# ## Eg1
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--disable-notifications')
#
# driver = webdriver.Chrome(options=opts)
# driver.implicitly_wait(10)
# ac_obj = ActionChains(driver)
#
# driver.get('https://www.linkedin.com')
# time.sleep(2)
#
# ## Locate the frame
# google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')
#
# ## switch the driver to the frame
# driver.switch_to.frame(google_frame)
#
# ## perform the operations inside the frame
# driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
# time.sleep(2)
#
# ## switch back to the parent frame
# driver.switch_to.parent_frame()
# time.sleep(2)
#
# ## scroll down till
# ele = driver.find_element('xpath', '//h2[contains(text(), "Join your colleagues")]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(2)
#
# ## locate the frame
# youtube_frame = driver.find_element('xpath', '//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
#
# ## switch thr driver to youtube_frame
# driver.switch_to.frame(youtube_frame)
# time.sleep(2)
#
# ## perform the oprations inside the frame
# driver.find_element('xpath', '//button[@title="Play"]').click()


#####################################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\iframe.html')
time.sleep(2)

## locate the iframe
frame1 = driver.find_element('xpath', '//iframe[@id="FR1"]')

## switch the driver to the frame
driver.switch_to.frame(frame1)

## perform the operations inside the frame
driver.find_element('xpath', '//input[@id="small-searchterms"]').send_keys('computers')
time.sleep(2)

## switch back to the parent frame
driver.switch_to.parent_frame()

## locate the frame2
frame2 = driver.find_element('xpath', '//iframe[@id="FR2"]')

## switch the driver to the frame
driver.switch_to.frame(frame2)
time.sleep(2)

## perform the operations inside the frame
driver.find_element('xpath', '//input[@id="search_form"]').send_keys('vehicle insurance')

## switch back to the parent frame
driver.switch_to.parent_frame()






















