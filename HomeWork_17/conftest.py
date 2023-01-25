import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session', autouse=False)
def chrome():
    yield webdriver.Chrome()


@pytest.fixture(scope='session', autouse=False)
def chrome_headless():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    yield webdriver.Chrome(chrome_options=options)