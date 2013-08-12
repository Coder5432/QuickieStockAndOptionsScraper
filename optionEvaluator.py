from OptionsScraper import scrapeEtf, scrapeLastUnderlyingPrice
from priceHistoryScraper import scrapePriceHistory
import datetime
import matplotlib.pyplot as plt
import numpy as np

def main():
    #88888888888888888888888888888888888888
    #chosenOption=
    #vxxOptions=scrapeEtf('VXX')
    closePriceHistory=scrapePriceHistory('VXX',['Date','Adj Close'])
    #cast priceHistory entries as dates and floats instead of strings.
    #returnRatios=getRatios(priceHistoryArray, "CalendarDays",30)
    priceCalendar=getAdjustedCalendar(closePriceHistory,"Interpolate Calendar Days")
    ratioResults=getColumn(priceCalendar,1)
    print(b)
    #ratioResults=getRatios(closePriceHistory, "Calendar Days",30)

def getRatios(priceHistory, spanMode, daySpan):
##    #main function to determine n-day returns on the
##    #stock or ETF over its price history.
##    #if spanMode is "Calendar Days" it  will
##    #get returns over the smallest trading day span exceeding the specified number
##    #of calendar days.
##    #if spanMode is "Trading Days", it will measure the span in trading days.
##    #if spanMode is "Interpolate Calendar Days" it will first interpolate prices
##    #over the trading day gaps, and then measure the span in exact calendar days.
    ratioResults=[]
##        currentDate=priceHistory[i][0]
##        futureDate=priceHistory[i+daySpan][0]
##        #gets the dateDifference in calendar days.
##        dateDifference=futureDate-currentDate
##        currentClose=float(priceHistory[i][1])
##        futureClose=float(priceHistory[i+daySpan][1])
##    priceRatio=futureClose/currentClose
##    #results array is made, indexed according to start date of each span.
##    ratioResultsEntry=[currentDate, dateDifference, priceRatio]
##    #check to make sure raw data passes filters.
##    #if priceHistory[i][1] > 20000000:
##    #    dayFailsFilter=True
##    ratioResults.append(ratioResultsEntry)
##    #print(spanResults)
    return ratioResults

def getAdjustedCalendar(priceHistory, spanMode):
    if spanMode=='Trading Days':
        return PriceHistory
    if spanMode=="Calendar Days":
        adjustedCalendar=[]
        for j in range(len(priceHistory)-1):
            startDate=priceHistory[j][0]
            startDatePrice=priceHistory[j][1]
            nextDate=priceHistory[j+1][0]
            dateDifference=(nextDate-startDate).days
            adjustedCalendar.append(priceHistory[j])
            if dateDifference > 1:
                for dateIndex in range(1,dateDifference):
                    insertionDate=startDate+datetime.timedelta(days=dateIndex)
                    adjustedCalendar.append([insertionDate,startDatePrice])
    if spanMode=="Interpolate Calendar Days":
        adjustedCalendar=[]
        for j in range(len(priceHistory)-1):
            startDate=priceHistory[j][0]
            startDatePrice=priceHistory[j][1]
            nextDate=priceHistory[j+1][0]
            nextDatePrice=priceHistory[j+1][1]
            dateDifference=(nextDate-startDate).days
            priceDifference=nextDatePrice-startDatePrice
            adjustedCalendar.append(priceHistory[j])
            if dateDifference > 1:
                for dateIndex in range(1,dateDifference):
                    insertionDate=startDate+datetime.timedelta(days=dateIndex)
                    fraction=dateIndex/dateDifference
                    interpolatedPrice=startDatePrice+fraction*priceDifference
                    adjustedCalendar.append([insertionDate,interpolatedPrice])
    return adjustedCalendar

def getColumn(matrix, i):
    return [row[i] for row in matrix]

def printArray(array):
    for i in range(len(array)):
        print(array[i])

def filterOptions(optionsArray, expiryYear='any', expiryMonth='any', expiryDay='any', callOrPut='any', strike='any', specialType='any'):
    acceptedEntries=[]
    for i in range(len(optionsArray)):
        disqualified=False
        if expiryYear != 'any':
            if optionsArray[i][3].year != expiryYear:
                disqualified=True
        if expiryMonth != 'any':
            if optionsArray[i][3].month != expiryMonth:
                disqualified=True
        if expiryDay != 'any':
            if optionsArray[i][3].day != expiryDay:
                disqualified=True
        if callOrPut != 'any':
            if optionsArray[i][4] != callOrPut:
                disqualified=True
        if strike != 'any':
            if optionsArray[i][2] != strike:
                disqualified=True
        if specialType != 'any':
            if optionsArray[i][7] != specialType:
                disqualified=True
        if disqualified==False:
            acceptedEntries.append(optionsArray[i])
    return acceptedEntries
                 
def getExpectedValue(option, ratios, currentUnderlyingPrice):
    #expects a row of the options array, the array of the ratios of
    #the underlying security's returns over eqivalent time periods as the time to expiry,
    #and the current price of the underlying security.
    dummy=2
    
            
#main()
print(scrapeLastUnderlyingPrice("TSLA"))
print('tesla')
b=scrapeEtf("VXX")
chosenOption=filterOptions(b,2015,1,17,"Put",17,"type 1")
#daysToExpiry=getDaysToExpiry(88888888888888888888888888888888888888888888

