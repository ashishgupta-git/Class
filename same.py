import time
from selenium import webdriver

search_words = ["Python", "Programming", "Microsoft", "Search", "Random"]

from selenium import webdriver

# Create an instance of Edge WebDriver
driver = webdriver.Edge()

# Rest of your code using the 'driver' object
# ...

# Close the browser window after the automation tasks
driver.quit()






# Configure Selenium WebDriver (ensure you have the appropriate browser driver)
driver = webdriver.Chrome()  # Change to appropriate driver (Chrome, Firefox, etc.)

def perform_search(word):
    driver.get("https://www.bing.com")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(word)
    search_box.submit()
    time.sleep(5)  # Wait for the search results to load

def start_search():
    for word in search_words:
        perform_search(word)
        time.sleep(10)  # Wait for 10 seconds before the next search

start_search()

# Close the browser window after the search is complete
driver.quit()
