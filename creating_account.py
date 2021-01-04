from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
import random
import string
from csv import writer
from time import sleep
from faker import Faker



# Random characters generators
def random_characters(y):
    return ''.join(random.choice(string.ascii_letters) for _x in range(y))


def random_hexdigits(y):
    return ''.join(random.choice(string.hexdigits) for _x in range(y))

driver = webdriver.Chrome()

# Go to URL:
url = 'http://automationpractice.com/index.php'
driver.get(url)
driver.maximize_window()

# Click 'Sign in'
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'login')))
sign_in_button = driver.find_element_by_class_name('login')
sign_in_button.click()

# Locate the 'Email address' field beneath 'CREATE AN ACCOUNT'
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'email_create')))
email_registration_field = driver.find_element_by_id('email_create')

# Generate and enter an email address
fake = Faker()
proper_email = fake.ascii_email()
email_registration_field.send_keys(proper_email)

# Locate the 'Create an account' button and click on it
create_account_button = driver.find_element_by_id('SubmitCreate')
create_account_button.click()

# === YOUR PERSONAL INFORMATION ===

# Account creation form is displayed
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'account-creation_form')))

# Select a radio button Mr. / Mrs.
radio_button_mr = driver.find_element_by_id('id_gender1')
radio_button_mr.click()

# Generate and enter firstname:
customer_firstname = driver.find_element_by_id('customer_firstname')
firstname = fake.first_name()
customer_firstname.send_keys(firstname)

# Generate and enter lastname:
customer_lastname = driver.find_element_by_id('customer_lastname')
lastname = fake.last_name()
customer_lastname.send_keys(lastname)

# Generate and enter password:
password_field = driver.find_element_by_id('passwd')
password = fake.password(10)
password_field.send_keys(password)

# The 'DATE OF BIRTH' dropdown

# Select a dropdown with days
dropdown_days = Select(driver.find_element_by_id('days'))

# The drop-down with days is displayed
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'uniform-days')))

# Select a day in range (1-28)
day_of_birth = random.randint(1, 28)
dropdown_days.select_by_index(day_of_birth)


# Select a dropdown with months
dropdown_months = Select(driver.find_element_by_id('months'))

# The drop-down with months is displayed
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'uniform-months')))

# Select a month in range (1-12)
month_of_birth = random.randint(0, 12)
dropdown_months.select_by_index(month_of_birth)

# Select a dropdown with years
dropdown_years = Select(driver.find_element_by_id('years'))

# The drop-down with years is displayed
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'uniform-years')))


# Select a year in range (1930-2002) by index
index_year = random.randint(19, 90)
dropdown_years.select_by_index(index_year)


# Create a dictionary from two lists - indexes and years:
def get_year_by_index(value):
    keys_list = list(range(19, 91))
    values_list = list(range(2002, 1930, -1))
    zip_iterator = zip(keys_list, values_list)
    year_dictionary = dict(zip_iterator)
    return year_dictionary[value]

year_of_birth = get_year_by_index(index_year)

# Full date of birth
date_of_birth = f'{day_of_birth}-{month_of_birth}-{year_of_birth}'


# Check in the newsletter checkbox
signup_for_newsletter = driver.find_element_by_id('newsletter')
signup_for_newsletter.click()

# Check in the 'Receive special offers' checkbox
receive_special_offers = driver.find_element_by_id('optin')
receive_special_offers.click()

# === YOUR ADDRESS ===

# Enter firstname:
firstname_your_address = driver.find_element_by_id('firstname')
firstname_your_address.send_keys(firstname)

# Enter lastname:
lastname_your_address = driver.find_element_by_id('lastname')
firstname_your_address.send_keys(lastname)

# Enter an address - first line
address_field = driver.find_element_by_id('address1')
address = fake.street_address()
address_field.send_keys(address)

# Enter a city
city_field = driver.find_element_by_id('city')
city = fake.city()
city_field.send_keys(city)

# Select a dropdown with States
dropdown_states = Select(driver.find_element_by_id('id_state'))

# The drop-down with States is displayed
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.ID, 'uniform-id_state')))

# Select a State by index 1-53
index_state = random.randint(1, 53)
dropdown_states.select_by_index(index_state)

# Create a dictionary {index: state}
index_state_dict = {1: 'Alabama', 2: 'Alaska', 3: 'Arizona', 4: 'Arkansas', 5: 'California', 6: 'Colorado', 7: 'Connecticut', 8: 'Delaware', 9: 'District of Columbia', 10: 'Florida', 11: 'Georgia', 12: 'Hawaii', 13: 'Idaho', 14: 'Illinois', 15: 'Indiana', 16: 'Iowa', 17: 'Kansas', 18: 'Kentucky', 19: 'Louisiana', 20: 'Maine', 21: 'Maryland', 22: 'Massachusetts', 23: 'Michigan', 24: 'Minnesota', 25: 'Mississippi', 26: 'Missouri', 27: 'Montana', 28: 'Nebraska', 29: 'Nevada', 30: 'New Hampshire', 31: 'New Jersey', 32: 'New Mexico', 33: 'New York', 34: 'North Carolina', 35: 'North Dakota', 36: 'Ohio', 37: 'Oklahoma', 38: 'Oregon', 39: 'Pennsylvania', 40: 'Puerto Rico', 41: 'Rhode Island', 42: 'South Carolina', 43: 'South Dakota', 44: 'Tennessee', 45: 'Texas', 46: 'US Virgin Islands', 47: 'Utah', 48: 'Vermont', 49: 'Virginia', 50: 'Washington', 51: 'West Virginia', 52: 'Wisconsin', 53: 'Wyoming'}

selected_state = index_state_dict[index_state]
sleep(3)
# Enter ZIP/Postal code
postcode_field = driver.find_element_by_id('postcode')
postcode = fake.postalcode()
postcode_field.send_keys(postcode)

# Enter mobile phone
phone_mobile_field = driver.find_element_by_id('phone_mobile')
phone_mobile = fake.random_number(10)
phone_mobile_field.send_keys(phone_mobile)

# Assign an address alias
alias_field = driver.find_element_by_id('alias')
alias = random_characters(5).lower()
alias_field.send_keys(alias)

# Locate the 'Register' button and click on it
register_button = driver.find_element_by_id('submitAccount')
register_button.click()

# === LOGOUT ===
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'logout')))
logout_button = driver.find_element_by_class_name('logout')
logout_button.click()

# Create list containing the user date generated/entered during registration
user_data = [proper_email, password, firstname, lastname, date_of_birth, address, city, selected_state, postcode, phone_mobile, alias]

# Append user_data as a new row to an existing user_data.csv file
with open('user_data.csv', 'a') as ud:
    writer_ud = writer(ud)
    writer_ud.writerow(user_data)
    ud.close()

# Print out user_data
print(f'\nUSER DATA:\nemail: {user_data[0]}\npassword: {user_data[1]}\nfirstname: {user_data[2]}\nlastname: {user_data[3]}\ndate of birth: {user_data[4]}\naddress: {user_data[5]}\ncity: {user_data[6]}\nstate: {user_data[7]}\npostcode: {user_data[8]}\nphone_mobile: {user_data[9]}\nalias: {user_data[10]}')

driver.close()
