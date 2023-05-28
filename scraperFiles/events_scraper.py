import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from scraperFiles.data import ScrapeData
from scraperFiles.filters import AddFilters
from scraperFiles.login import Login


class Times(webdriver.Chrome):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Times, self).__init__(service=Service(ChromeDriverManager().install()), options=self.options)

    def login(self, email):
        login = Login(self)
        login.login(email)

    def add_filters(self, category, location, formats):
        filters = AddFilters(self)
        if formats != "":
            filters.add_format(formats)
        if location != "":
            filters.add_location(location)
        if category != "":
            filters.add_category(category)

    def get_all_links(self):
        all_links_tag = self.find_elements(By.CSS_SELECTOR, 'a[data-ga-action="Event Listing | Event Snippet"]')
        all_links = [a.get_attribute('href') for a in all_links_tag]
        self.quit()
        return all_links

    def get_data(self):
        with open('data.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Event Url', 'Event Name', 'Event Date', 'Event Time', 'Event Location', 'Event Fee',
                                 'Event Sector', 'Event Organizer', 'Total Event', 'Event Followers', 'Event Exhibitors',
                                 'Event Speakers', 'Event Company Profile', 'Scrape Date'])
        print("*" * 10 + "data scraping has started" + "*" * 10)
        for link in self.get_all_links():
            data = ScrapeData(link)
            data.convert_to_csv()
        print("*"*10 + "finished scraping" + "*"*10)
