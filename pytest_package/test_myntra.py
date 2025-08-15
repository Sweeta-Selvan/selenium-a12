import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)



# @pytest.fixture(scope = 'class')
# def launch():
#     driver = webdriver.Chrome(opts)
#     ac_obj = ActionChains(driver)
#     driver.get('https://www.myntra.com/')
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     yield driver
    

# @pytest.mark.xfail
# class TestShopping:
#     def test_search(self, launch):
#         launch.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
#     def test_choose(self, launch):
#         launch.find_element('xpath', '//li[text() = "Adidas Bags"]').click()
#     def test_categories(self, launch):
#         launch.find_element('xpath', '//label[text() = "Backpacks"]').click()
#     def test_filter(self, launch):
#         ele = launch.find_element('xpath', '//span[@class="myntraweb-sprite sort-downArrow sprites-downArrow"]').click()
#         ActionChains(launch).move_to_element(ele).perform()
#     def test_sort(self, launch):
#         launch.find_element('xpath', '//input[@value="popularity"]').click()
#     def test_bundles(self, launch):
#         launch.find_element('xpath', '//span[@class="atsa-downArrow sprites-arrowDownBold myntraweb-sprite"]').click()
#     def test_selectbundles(self,launch):
#         launch.find_element('xpath', '//label[text() = "Single Styles"]').click()
    
# class TestShop:
#     def test_women(self, launch):
#         launch.find_element('xpath', '//a[text() = "Women"]').click()
#     def test_dresses(self, launch):
#         launch.find_element('xpath', '//a[text() = "Dresses"]').click()

@pytest.mark.parametrize('a, b',[(1,2), (9,3), (4,5)])
def test_add(a, b):
    print(a+b)