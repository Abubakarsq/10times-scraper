from scraperFiles.events_scraper import Times

times_bot = Times()
email = input("please enter your email address:\t")
times_bot.login(email)
filters = input("Do you want to add filters (yes or no)").lower()
if filters == "yes":
    category = input("enter the category (leave it blank if you don't want to specify):\t").capitalize()
    location = input("enter the location (leave it blank if you don't want to specify):\t").capitalize()
    formats = input("enter the format (workshops, conferences, trade shows) (leave it blank if you don't want to specify):\t").capitalize()
    times_bot.add_filters(category=category, location=location, formats=formats)


if __name__ == "__main__":
    times_bot.get_all_links()
    times_bot.get_data()
