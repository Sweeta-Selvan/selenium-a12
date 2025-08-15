# import time
# from selenium import webdriver
# chrome_driver=webdriver.Chrome()
# time.sleep(10)

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# c_driver=webdriver.Chrome(opts)

# import time
# from selenium import webdriver
# firefox_driver=webdriver.Firefox()

# import time
# from selenium import webdriver
# edge_driver=webdriver.Edge()
# time.sleep(10)

# from selenium import webdriver
# opts=webdriver.EdgeOptions()
# opts.add_experimental_option("detach", True)
# e_driver=webdriver.Edge(opts)
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
# # launch app
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# print(driver.current_url)
# print(driver.title)
# print(driver.name)
# driver.maximize_window()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(2)
# driver.save_screenshot(r"C:\Users\Rajan Quvae\Desktop\selenium_training\training\screenshots\myn.png")
# driver.close()
import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)

class Register:

    driver.get('https://www.facebook.com/')
    time.sleep(2)
    driver.find_element('name','email').send_keys('sweet@gmail.com')
    time.sleep(2)
    driver.find_element('name','pass').send_keys('4321')
                                              