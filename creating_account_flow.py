from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import  Select
from selenium.common.exceptions import *
import random
import string
from time import sleep

# Random characters generators
def random_characters(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def random_hexdigits(y):
    return ''.join(random.choice(string.hexdigits) for x in range(y))

driver = webdriver.Chrome()
url = 'http://automationpractice.com/index.php'

# Go to URL:
driver.get(url)

# Click 'Sign in'
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'login')))
sign_in_button = driver.find_element_by_class_name('login')
sign_in_button.click()

# Locate the 'Email address' field beneath 'CREATE AN ACCOUNT'
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'email_create')))
email_registration_field = driver.find_element_by_id('email_create')

# Generate a proper email address
proper_email = random_characters(12) + '@4t6.pl'
print('email: ', proper_email)

# Enter a generated email to the 'Email address' field
email_registration_field.send_keys(proper_email)
sleep(1)

# Locate the 'Create an account' button and click on it
create_account_button = driver.find_element_by_id('SubmitCreate')
create_account_button.click()

# Account creation form is displayed
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'account-creation_form')))

# Select a radio button Mr. / Mrs.
radio_button_mr = driver.find_element_by_id('id_gender1')
radio_button_mr.click()
sleep(1)
# Generate and enter firstname:
customer_firstname = driver.find_element_by_id('customer_firstname')
firstname = random_characters(1).upper() + random_characters(5).lower()
print('Firstname: ', firstname)
customer_firstname.send_keys(firstname)

# Generate and enter lastname:
customer_lastname = driver.find_element_by_id('customer_lastname')
lastname = random_characters(1).upper() + random_characters(5).lower()
print('Lastname: ', lastname)
customer_lastname.send_keys(lastname)

# Generate and enter password:
password_field = driver.find_element_by_id('passwd')
password = random_hexdigits(8)
print('Password: ', password)
password_field.send_keys(password)

# The 'DATE OF BIRTH' dropdown

# Select a dropdown with days
dropdown_days = Select(driver.find_element_by_id('days'))

# The drop-down with days is displayed
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'uniform-days')))

# Select a day in range (1-28)
day_of_birth = random.randint(1, 28)
dropdown_days.select_by_index(day_of_birth)
sleep(1)
# Select a dropdown with months
dropdown_months = Select(driver.find_element_by_id('months'))

# The drop-down with months is displayed
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'uniform-months')))

# Select a month in range (1-12)
month_of_birth = random.randint(0, 12)
dropdown_months.select_by_index(month_of_birth)
sleep(1)
# Select a dropdown with years
dropdown_years = Select(driver.find_element_by_id('years'))

# The drop-down with years is displayed
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'uniform-years')))

# dropdown_years_list = driver.find_element_by_id('uniform-years')
# actions = ActionChains(driver)
# actions.move_to_element(dropdown_years_list).perform()

# Select a year in range (1930-2002)
year_of_birth = random.randint(19, 90)
dropdown_years.select_by_index(year_of_birth)

# Create a dictionary from two lists - indexes and years:
keys_list = list(range(19, 91))
values_list = list(range(2002, 1930, -1))
zip_iterator = zip(keys_list, values_list)
year_dictionary = dict(zip_iterator)

print(f'Day of birth: {day_of_birth}-{month_of_birth}-{year_dictionary[year_of_birth]}')

sleep(3)
driver.close()