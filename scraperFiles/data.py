import datetime as dt
import csv
import requests
from bs4 import BeautifulSoup
from scraperFiles.error_checker import ErrorChecker


class ScrapeData(ErrorChecker):
    now = dt.datetime.now()

    def __init__(self, link):
        self.link = link.strip()
        self.event_response = requests.get(url=self.link)

    def webpage(self):
        try:
            event_html = self.event_response.text
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectTimeout, requests.exceptions.SSLError,
                requests.exceptions.ConnectionError):
            return None

        event_soup = BeautifulSoup(event_html, 'html.parser')
        return event_soup

    def get_event_name(self):
        event_name_tag = self.webpage().find('h1')
        event_name = self.check_error3(event_name_tag)
        return event_name

    def get_date_and_time(self):
        date_of_event = self.check_error1(self.webpage())
        time_of_event = self.check_error2(self.webpage())
        return date_of_event, time_of_event

    def get_location(self):
        location_of_event_tag = self.webpage().find('a', attrs={"class": 'bld text-decoration-none'})
        location_of_event = self.check_error3(location_of_event_tag)

        return location_of_event

    def get_fee(self):
        fee_tag = self.webpage().find('td', attrs={"style": 'width:50%;'})
        fee = self.check_error5(fee_tag)
        return fee

    def get_event_sector(self):
        event_sector_tag = self.webpage().select_one(selector='#hvrout2 a')
        event_sector = self.check_error3(event_sector_tag)
        return event_sector

    def get_organiser(self):
        organiser_tag = self.webpage().find(id='org-name')
        organiser = self.check_error3(organiser_tag)
        return organiser

    def get_total_event(self):
        total_events_tag = self.webpage().find('span', attrs={'class': 'text-muted fw-bold'})
        total_events = self.check_error3(total_events_tag)
        return total_events

    def get_followers(self):
        followers_tag = self.webpage().select_one(selector='#visitors span')
        followers = self.check_error3(followers_tag)
        return followers

    def get_exhibitors(self):
        exhibitors_tag = self.webpage().select_one(selector='#exhibitors span')
        exhibitors = self.check_error3(exhibitors_tag)
        return exhibitors

    def get_speakers(self):
        speakers_tag = self.webpage().select_one(selector='#speakers span')
        speakers = self.check_error3(speakers_tag)
        return speakers

    def get_company_profile(self):
        company_profile_tag = self.webpage().find(id='org-name')
        company_profile = self.check_error4(company_profile_tag)
        return company_profile

    def convert_to_csv(self):
        event_date, event_time = self.get_date_and_time()
        with open('data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([self.link.strip(), self.get_event_name(), event_date, event_time,
                                 self.get_location(), self.get_fee(), self.get_event_sector(), self.get_organiser(),
                                 self.get_total_event(), self.get_followers(), self.get_exhibitors(),
                                 self.get_speakers(),
                                 self.get_company_profile(),
                                 f'{self.now.strftime("%d")} - {self.now.strftime("%m")} - {self.now.strftime("%Y")}'])
