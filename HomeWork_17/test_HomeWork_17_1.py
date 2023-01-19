from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

FULL_NAME_FIELD = '//input[@id="userName"]'
EMAIL_FIELD = '//input[@id="userEmail"]'
CURRENT_ADDRESS_FIELD = '//textarea[@id="currentAddress"]'
PERMANENT_ADDRESS_FIELD = '//textarea[@id="permanentAddress"]'
SUBMIT_BUTTON = '//button[@id="submit"]'


def test_form(chrome):
    driver = chrome
    driver.get('https://demoqa.com/text-box')
    name = driver.find_element(By.XPATH, FULL_NAME_FIELD)
    email = driver.find_element(By.XPATH, EMAIL_FIELD)
    current_address = driver.find_element(By.XPATH, CURRENT_ADDRESS_FIELD)
    permanent_address = driver.find_element(By.XPATH, PERMANENT_ADDRESS_FIELD)
    submit = driver.find_element(By.XPATH, SUBMIT_BUTTON)

    name.send_keys('Oleksandr Lobov')
    email.send_keys('test@gmail.com')
    current_address.send_keys('Cherkasy Gogolya str.')
    permanent_address.send_keys('Cherkasy Himka prov.')
    driver.execute_script('window.scrollTo(0, 500)')
    submit.click()

    name_text = name.get_attribute('value')
    email_text = email.get_attribute('value')
    curr_add_text = current_address.get_attribute('velue')
    per_add_text = permanent_address.get_attribute('velue')

    result_name = driver.find_element(By.ID, 'name').text
    result_email = driver.find_element(By.ID, 'email').text
    result_ca = driver.find_element(By.XPATH, '//p[@id="currentAddress"]').text
    result_pa = driver.find_element(By.XPATH, '//p[@id="permanentAddress"]').text
    pass