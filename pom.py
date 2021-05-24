from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# When the website www.makemytrip.com is displayed
url = 'http://www.makemytrip.com'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)


# And the round trip in the flights link is selected
def round_trip_btn():
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "li[data-cy='roundTrip']"))
    )
    element.click()
    return None

# TODO: And the selection from Delihi is made
def from_text_field():
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ))
    )


# TODO: And the selection to Bangalore is made
def dest_text_field():
    pass

# TODO: And the departure date (today's date) is made
def departure_date():
    pass

# TODO: And the return date (7 days later than departure) is made
def returning_date():
    pass

# TODO: Then the search button is clicked
def search_btn():
    pass

# TODO: Then the total number of records 'Departure Flight' and 'Return Flight' is printed on the console
def number_of_records():
    pass

# TODO: Then the Non-Stop and 1 Stop filter options and print total number of records of 'Departure Flight,
#  and 'Return flight' is printed on the console
def nonstop_and_onestop():
    # prints to console
    pass

# TODO: Then the radio button on the departure flightis selected
def departure_flight_selection():
    pass

# TODO: Then the radio button on the return flight is selected
def return_flight_selection():
    pass

# TODO: Assert the correct cumulative monetary amount is correct in the bottom right of the bar


round_trip_btn()
time.sleep(3)
browser.quit()
