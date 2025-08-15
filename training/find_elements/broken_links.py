from selenium import webdriver
import requests

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(opts)
driver.implicitly_wait(15)
# driver.get('https://www.ikea.com/')

# all_links = driver.find_elements('tag name', 'a')
# # print(all_links)

# for ele in all_links:
#     link = ele.get_attribute('href')
#     # print(link)
#     try:
#         info = requests.head(link)
#         if info.status_code!= 200:
#             print(link, '=' , info.status_code)
#     except:
#         continue

############################################################################################################
driver.get('https://www.firstcry.com/')
fetch_we = driver.find_elements('tag name', 'a')
for ele in fetch_we:
    link = ele.get_attribute('href')
    try:
        info = requests.head(link)
        if info.status_code!= 200:
            print(link, '=' , info.status_code)
    except:
        continue

