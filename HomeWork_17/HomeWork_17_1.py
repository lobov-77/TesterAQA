import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

FULL_NAME_FIELD = '//input[@id="userName"]'
EMAIL_FIELD = '//input[@id="userEmail"]'
CURRENT_ADDRESS_FIELD = '//textarea[@id="currentAddress"]'
PERMANENT_ADDRESS_FIELD = '//textarea[@id="permanentAddress"]'
SUBMIT_BUTTON = '//button[@id="submit"]'

driver = Chrome()


@pytest.fixture
def text_fields():
    driver.get('https://demoqa.com/text-box')


def test_form(text_fields):
    name_field = driver.find_element(By.XPATH, FULL_NAME_FIELD)
    email_field = driver.find_element(By.XPATH, EMAIL_FIELD)
    current_address_field = driver.find_element(By.XPATH, CURRENT_ADDRESS_FIELD)
    permanent_address_field = driver.find_element(By.XPATH, PERMANENT_ADDRESS_FIELD)
    submit_button = driver.find_element(By.XPATH, SUBMIT_BUTTON)

    name_field.send_keys('Oleksandr Lobov')
    email_field.send_keys('test@gmail.com')
    current_address_field.send_keys('Cherkasy Gogolya str.')
    permanent_address_field.send_keys('Cherkasy Himka prov.')
    driver.execute_script('window.scrollTo(0, 500)')
    submit_button.click()

    name_field_text = name_field.get_attribute('value')
    email_field_text = email_field.get_attribute('value')
    curr_add_field_text = current_address_field.get_attribute('value')
    per_add_field_text = permanent_address_field.get_attribute('value')

    result_name_field = driver.find_element(By.ID, 'name').text.split(':')[1]
    result_email_field = driver.find_element(By.ID, 'email').text.split(':')[1]
    result_ca_field = driver.find_element(By.XPATH, '//p[@id="currentAddress"]').text.split(':')[1]
    result_pa_field = driver.find_element(By.XPATH, '//p[@id="permanentAddress"]').text.split(':')[1]

    assert_data_fields = [result_name_field == name_field_text, result_email_field == email_field_text,
                          result_ca_field == curr_add_field_text,
                          result_pa_field == per_add_field_text]
    assert all(assert_data_fields)


def test_invalid_email(text_fields):
    email_field = driver.find_element(By.XPATH, EMAIL_FIELD)
    submit_button = driver.find_element(By.XPATH, SUBMIT_BUTTON)

    email_field.send_keys('test')
    driver.execute_script('window.scrollTo(0, 500)')
    submit_button.click()

    email_field_error = driver.find_element(By.XPATH, '//input[@class="mr-sm-2 field-error form-control"]')
    assert email_field_error.is_displayed()



