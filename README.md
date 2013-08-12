Quickie! Stock and Options Scraper
===============

Financial stock and options data scraper project using Yahoo! Finance, written in Python 3

as of 8/8/2013, I'm still learning GIT.  so let me GET this stuff up here using GIT before you GIT too ornery about the fact that the files aren't online yet.

This provides a tool for gathering both historical stock data from the Yahoo! finance API, but also a tool to scrape the current options prices and bidding data for any given listed stock.  And on top of that, there's even a tool to look at the expected future values of options based on historical volatility!  Pretty neat, eh?


##Dependencies

PriceHistoryScraper.py relies only on native Python 3 libraries, and requires no dependencies.

OptionsScraper.py depends on version 4 or above of the Beautiful Soup package (learn more at http://www.crummy.com/software/BeautifulSoup/).


##Nice Things To Know

This project was developed with the initial purpose of using historical price movement trends to evaluate the probability distribution (and corresponding expected value) of stock options prices at expiry, based on historical price movements of the underlying stock or ETF.  This is an analysis strategy that doesn't need up-to-the-second data, and as such, a relatively slow source of data, Yahoo Finance, could be used.  Keeping this in mind, know that you shouldn't expect any options data pulled from OptionsScraper.py to be the freshest- it will probably be 15 minute old data.  If you need super-fresh data, it looks like you probably have to use a more sophisticated setup.

On top of that, if you do use this scraper, it would probably be a good idea not to ping Yahoo's servers too badly.  Use your best judgement here.

If you are looking for up-to-the-second data for hyper-quick algo trading, this isn't the stuff that you need.
