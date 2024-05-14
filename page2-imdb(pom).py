from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from imdbpom import IMDbSearchPage

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open IMDb search page
driver.get("https://www.imdb.com/search/name/")

# Initialize IMDbSearchPage
imdb_search_page = IMDbSearchPage(driver)

# Fill all fields
imdb_search_page.enter_search_query("Brad Pitt")
# (You can fill other fields in a similar way using methods in the IMDbSearchPage class)

# Click the search button
imdb_search_page.click_search_button()

# Wait for search results to load (example)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "lister-list"))
)

# Further actions with search results (e.g., scraping)
# ...

# Close the WebDriver
driver.quit()