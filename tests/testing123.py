import hockey_scraper

# Scrapes the first game of 2014, 2015, and 2016 seasons with shifts and stores the data in a Csv file
hockey_scraper.scrape_games([2014020001, 2015020001, 2016020001], True)

# Scrapes the first game of 2007, 2008, and 2009 seasons with shifts and returns a Dictionary with the Pandas DataFrames
scraped_data = hockey_scraper.scrape_games([2007020001, 2008020001, 2009020001], True, data_format='Pandas')

print(scraped_data)