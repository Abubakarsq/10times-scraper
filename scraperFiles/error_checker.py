
class ErrorChecker:
    @staticmethod
    def check_error1(event):
        try:
            date_of_event_tag0 = event.find('span', attrs={'class': 'ms-1'})
            if 'Followers' in date_of_event_tag0.text:
                date_of_event_tag1 = event.select_one(selector='span.headereventDate')
                date_of_event1 = date_of_event_tag1.get('data-end-date')
                return date_of_event1
            return date_of_event_tag0.text
        except AttributeError:
            return 'n/a'

    @staticmethod
    def check_error2(event):
        try:
            time_of_event_tag0 = event.find('td', attrs={"style": 'width: 50%;'})
            return time_of_event_tag0.text.split('\n')[0]
        except AttributeError:
            try:
                time_of_event_tag1 = event.select_one(selector='span.headereventDate')
                time_of_event1 = time_of_event_tag1.get('data-start-time') + '-' + time_of_event_tag1.get(
                    'data-end-time')
                return time_of_event1
            except AttributeError:
                return 'n/a'

    @staticmethod
    def check_error3(event_tag):
        try:
            return event_tag.text
        except AttributeError:
            return 'n/a'

    @staticmethod
    def check_error4(event_tag):
        try:
            return event_tag.get('href')
        except AttributeError:
            return 'n/a'

    @staticmethod
    def check_error5(event_tag):
        try:
            return event_tag.text.split('\n')[1].strip()
        except (IndexError, AttributeError):
            return 'n/a'
