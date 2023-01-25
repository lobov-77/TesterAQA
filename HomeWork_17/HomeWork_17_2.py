import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

FULL_NAME_FIELD = 'input#userName'
EMAIL_FIELD = 'input#userEmail'
CURRENT_ADDRESS_FIELD = 'textarea#currentAddress'
PERMANENT_ADDRESS_FIELD = 'textarea#permanentAddress'
SUBMIT_BUTTON = 'button#submit'

driver = Chrome()


@pytest.fixture
def text_fields():
    driver.get('https://demoqa.com/text-box')


def test_form(text_fields):
    driver.get('https://demoqa.com/text-box')
    name_field = driver.find_element(By.CSS_SELECTOR, FULL_NAME_FIELD)
    email_field = driver.find_element(By.CSS_SELECTOR, EMAIL_FIELD)
    current_address_field = driver.find_element(By.CSS_SELECTOR, CURRENT_ADDRESS_FIELD)
    permanent_address_field = driver.find_element(By.CSS_SELECTOR, PERMANENT_ADDRESS_FIELD)
    submit_button = driver.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON)

    name_field.send_keys('Oleksandr Lobov')
    email_field.send_keys('test@gmail.com')
    current_address_field.send_keys('Cherkasy Gogolya str.')
    permanent_address_field.send_keys('Cherkasy Himka prov.')
    driver.execute_script('window.scrollTo(0, 500)')
    submit_button.click()

    name_filed_text = name_field.get_attribute('value')
    email_filed_text = email_field.get_attribute('value')
    curr_add_filed_text = current_address_field.get_attribute('value')
    per_add_filed_text = permanent_address_field.get_attribute('value')

    result_name_filed = driver.find_element(By.CSS_SELECTOR, 'p[id=name]').text.split(':')[1]
    result_email_filed = driver.find_element(By.CSS_SELECTOR, 'p[id=email]').text.split(':')[1]
    result_ca_filed = driver.find_element(By.CSS_SELECTOR, 'p[id="currentAddress"]').text.split(':')[1]
    result_pa_filed = driver.find_element(By.CSS_SELECTOR, 'p[id="permanentAddress"]').text.split(':')[1]

    assert_data_fields = [result_name_filed == name_filed_text, result_email_filed == email_filed_text,
                          result_ca_filed == curr_add_filed_text,
                          result_pa_filed == per_add_filed_text]

    assert all(assert_data_fields)


def invalid_email(text_fields):
    driver.get('https://demoqa.com/text-box')
    email_field = driver.find_element(By.CSS_SELECTOR, EMAIL_FIELD)
    submit_button = driver.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON)

    email_field.send_keys('test')
    driver.execute_script('window.scrollTo(0, 500)')
    submit_button.click()

    email_field_error = driver.find_element(By.CSS_SELECTOR, 'input[class="mr-sm-2 field-error form-control"]')
    assert email_field_error.is_displayed()
