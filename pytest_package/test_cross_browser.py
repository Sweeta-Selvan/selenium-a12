import pytest
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

@pytest.fixture(scope = 'class', params= ['chrome', 'firefox', 'edge'])
def launch(request):
    parameter= request.param
    if parameter == 'chrome':
        driver = webdriver.Chrome(opts)
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    
    elif parameter == 'edge':
        driver = webdriver.Edge()

    driver.get('https://www.myntra.com/')
    yield driver

class TestShopping:
    def test_search(self, launch):
        launch.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
 