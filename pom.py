from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()


class MonetaryAddition:
    def __init__(self, driver):
        # Given the website www.makemytrip.com is displayed
        self.driver = driver
        self.url = 'http://www.makemytrip.com'

    def go(self):
        self.browser(self.url)


    # And the round trip in the flights link is selected
    def round_trip_btn(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li[data-cy='roundTrip']"))
        )
        element.click()
        return None

    # TODO: And the selection from Delihi is made
    def from_text_field(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              'input[class="react-autosuggest__input react-autosuggest__input--open"]'))
        )
        element.send_keys("Yo")

    # TODO: And the selection to Bangalore is made
    def dest_text_field(self):
        pass

    # TODO: And the departure date (today's date) is made
    def departure_date(self):
        pass

    # TODO: And the return date (7 days later than departure) is made
    def returning_date(self):
        pass

    # TODO: Then the search button is clicked
    def search_btn(self):
        pass

    # TODO: Then the total number of records 'Departure Flight' and 'Return Flight' is printed on the console
    def number_of_records(self):
        pass

    # TODO: Then the Non-Stop and 1 Stop filter options and print total number of records of 'Departure Flight,
    #  and 'Return flight' is printed on the console
    def nonstop_and_onestop(self):
        # prints to console
        pass

    # TODO: Then the radio button on the departure flightis selected
    def departure_flight_selection(self):
        pass

    # TODO: Then the radio button on the return flight is selected
    def return_flight_selection(self):
        pass

    # TODO: Assert the correct cumulative monetary amount is correct in the bottom right of the bar


browser.maximize_window()
testing_page = MonetaryAddition(driver=browser)
testing_page.go()
# # round_trip_btn()
# # time.sleep(3)
# # browser.quit()
