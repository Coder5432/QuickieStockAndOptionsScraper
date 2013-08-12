from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request

def scrapePriceHistory(symbol,chosenColumns):
    potentialColumns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    priceHistoryUrl="http://ichart.finance.yahoo.com/table.csv?s="+symbol+"&g=d&ignore=.csv"
    priceHistoryResponse=urllib.request.urlopen(priceHistoryUrl)
    returnedArray=str(priceHistoryResponse.read(),encoding='utf8').split('\n')
    reversePriceHistoryArray=[]
    for i in range(1,len(returnedArray)-1):
        temp1=[]
        temp2=[]
        temp1=returnedArray[i].split(',')
        #convert column 0 to date, columns 1-4 to float, 5 to int, 6 to float
        temp1[0]=datetime.strptime(temp1[0],"%Y-%m-%d")
        temp1[1]=float(temp1[1])
        temp1[2]=float(temp1[2])
        temp1[3]=float(temp1[3])
        temp1[4]=float(temp1[4])
        temp1[5]=int(temp1[5])
        temp1[6]=float(temp1[6])
        for j in range(len(chosenColumns)):
            for k in range(len(potentialColumns)):
                if chosenColumns[j]==potentialColumns[k]:
                    temp2.append(temp1[k])
        reversePriceHistoryArray.append(temp2)
    #priceHistory Array format by row:
    #['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    priceHistoryArray=reversePriceHistoryArray[::-1]
    return priceHistoryArray
