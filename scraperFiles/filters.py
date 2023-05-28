from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AddFilters:
    def __init__(self, driver):
        self.driver = driver

    def add_location(self, location):
        collapsed_button = self.driver.find_element(By.CSS_SELECTOR, "#location button")
        if "collapsed" in collapsed_button.get_attribute("class"):
            collapsed_button.click()
        location_search = self.driver.find_element(By.ID, "LocationSearch")
        location_search.clear()
        location_search.send_keys(location)
        location_search.send_keys(Keys.ENTER)

    def add_format(self, formats):
        collapsed_button = self.driver.find_element(By.CSS_SELECTOR, "#format button")
        if "collapsed" in collapsed_button.get_attribute("class"):
            collapsed_button.click()
        format_checkbox = self.driver.find_element(By.CSS_SELECTOR,
                                                   f"#by-format a[data-ga-label='Event Listing | Filter | {formats}']")
        format_checkbox.click()

    def add_category(self, category):
        collapsed_button = self.driver.find_element(By.CSS_SELECTOR, "#category button")
        if "collapsed" in collapsed_button.get_attribute("class"):
            collapsed_button.click()
        category_search = self.driver.find_element(By.ID, "IndustrySearch")
        category_search.clear()
        category_search.send_keys(category)
        category_search.send_keys(Keys.ENTER)
