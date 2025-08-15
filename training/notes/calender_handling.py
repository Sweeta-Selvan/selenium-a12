import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.makemytrip.com/')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# # while True:
# #     try:
# #         driver.find_element('xpath', '//div[text()="January 2026"]/../..//p[text()="15"]').click()
# #         break
# #     except:
# #         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#
#
# def select_date(month, date):
#     while True:
#         try:
#             driver.find_element('xpath', f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
#             break
#         except:
#             driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#
#
# select_date('May 2026', '21')

#############################################################################################################

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.makemytrip.com/')
driver.maximize_window()
time.sleep(2)
driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
time.sleep(2)
driver.find_element('xpath', '//span[text()="Departure"]').click()
time.sleep(2)

# while True:
#     month = driver.find_element('xpath', '(//div[@class="DayPicker-Caption"])[1]')       ## common xpath for left side and right side months
#     print(month.text)           ##  July 2025
#
#     if month.text == 'April 2026':      ## July == April
#         driver.find_element('xpath', '(//p[text()="10"])[1]').click()
#         break
#     else:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()        ## clicking on right arrow
#

##--------------------------------------------------------------------------------

for i in range(1, 13):
    month = driver.find_element('xpath', '(//div[@class="DayPicker-Caption"])[1]')       ## common xpath for left side and right side months
    print(month.text)           ##  July 2025

    if month.text == 'April 2026':      ## July == April
        driver.find_element('xpath', '(//p[text()="10"])[1]').click()
        break
    else:
        driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()        ## clicking on right arrow



























































































