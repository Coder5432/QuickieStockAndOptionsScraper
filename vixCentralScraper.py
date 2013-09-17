from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://www.vixcentral.com") # Load page
assert "VIX Term Structure" in browser.title
try:
    historicalButton=browser.find_element_by_id("ui-id-4")
except NoSuchElementException:
    assert 0, "could not find historical prices button"
print('historical button located.')
historicalButton.click()
print('clicked.')
dateField=browser.find_element_by_id("date1")
getPricesButton=browser.find_element_by_id("b4")
time.sleep(2)
dateField.clear()
dateField.send_keys("January 1, 2013")
time.sleep(2)
getPricesButton.click()
