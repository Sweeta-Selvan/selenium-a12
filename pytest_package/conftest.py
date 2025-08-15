# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)



# @pytest.fixture(scope='class')
# def browser():
#     driver = webdriver.Chrome(opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     driver.implicitly_wait(20)
#     yield driver

# @pytest.fixture(scope = 'class')
# def launch():
#     driver = webdriver.Chrome(opts)
#     ac_obj = ActionChains(driver)
#     driver.get('https://www.myntra.com/')
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     yield driver
    
