from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.ID, "navbar-query")
        self.search_button = (By.ID, "navbar-submit-button")

    def enter_search_query(self, query):
        search_bar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.search_bar))
        search_bar.clear()
        search_bar.send_keys(query)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button))
        search_button.click()