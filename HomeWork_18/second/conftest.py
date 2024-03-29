import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('--window-size=1080,1080')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://demoqa.com/dynamic-properties'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver


@pytest.fixture(scope='function', autouse=True)
def start_end_test():
    print('\nThis is start')
    yield
    print('\nFinish')


@pytest.fixture(scope='function')
def get_id(setup):
    element = setup.find_element(By.XPATH, '//p[contains(text(), "random")]')
    yield element.get_attribute('id')




