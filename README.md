Quickie! Stock and Options Scraper
===============

A financial stock and options data scraper project using Yahoo! Finance, written in Python 3.

More documentation coming soon.  Also, this isn't done yet, coding wise, so hold your horses unless you're willing to trudge through the bugs.

This provides a tool for gathering both historical stock data from the Yahoo! finance API, but also a tool to scrape the current options prices and bidding data for any given listed stock.  And on top of that, there's even a tool to look at the expected future values of options based on historical price movements!  Pretty neat, eh?

##Usage
You may use this to do a couple different things.  Each of the three files included in this repo are responsible for a group of related tasks.  You may use the functions in optionsScraper.py to scrape and filter option chain data, with the latest prices for each option.  Example:

To scrape options chain data, using optionsScraper.py:
  scrapeOption("MSFT")
  #[['MSFT', 'MSFT150117C00015000', 15.0, datetime.date(2015, 1, 17), 'Call', '17.10', -0.75, 'type 1'], ['MSFT', 'MSFT150117C00018000', 18.0, datetime.date(2015, 1, 17), 'Call', '14.85', 0.0, 'type 1'],.......]
  #

To scrape price history data, using priceHistoryScraper.py:
  hist=scrapePriceHistory("GOOG",["Date","Adj Close"])
  #[[datetime.datetime(2004, 8, 19, 0, 0), 100.34], [datetime.datetime(2004, 8, 20, 0, 0), 108.31],........]

##Dependencies

PriceHistoryScraper.py relies only on native Python 3 libraries, and requires no dependencies.

OptionsScraper.py depends on version 4 or above of the Beautiful Soup package (learn more at http://www.crummy.com/software/BeautifulSoup/).


##Nice Things To Know

This project was developed with the initial purpose of using historical price movement trends to evaluate the probability distribution (and corresponding expected value) of stock options prices at expiry, based on historical price movements of the underlying stock or ETF.  This is an analysis strategy that doesn't need up-to-the-second data, and as such, a relatively slow source of data, Yahoo Finance, could be used.  Keeping this in mind, know that you shouldn't expect any options data pulled from OptionsScraper.py to be the freshest- it will probably be 15 minute old data.  If you need super-fresh data, it looks like you probably have to use a more sophisticated setup.

On top of that, if you do use this scraper, it would probably be a good idea not to ping Yahoo's servers too badly.  Use your best judgement here.

If you are looking for up-to-the-second data for hyper-quick algo trading, this isn't the stuff that you need.
