#todo:
#continue parsing each option.  right now dailyvalue change is last bit completed.
#order stuff into optionsResults in a reasonable way.

from bs4 import BeautifulSoup
import urllib.request
from datetime import date
import datetime
from re import search


def scrapeEtf(etfName):
    urlBase='http://finance.yahoo.com'
    #urlIndex is iterated at every different expiry month (when the expiry month links are traversed.)
    urlIndex=0
    currentEtfCompleted=False
    #-------------------------------begin url loop:-------------------------------------
    while currentEtfCompleted==False:
        if urlIndex==0:
            #print('expiry month number 1 is being scraped.')
            urlSuffix=urlSuffix='/q/op?s='+etfName+'+Options'
            #print('scraping from initial URL: '+urlBase+urlSuffix)
            urlIndex=urlIndex+1
        else:
            urlIndex=urlIndex+1
            #use the html from the previous loop to get the link for the next expiry month.
            #print('expiry month number '+str(urlIndex)+' is being scraped.')
            currentMonth=maintd.find('strong')
            #get two siblings over.  It might be the next expiry month.  If string length is 6 (formatted ex. May 13) then it
            #is the next expiry month.
            potentialNextMonth=maintd.find('strong').next_sibling.next_sibling
            if potentialNextMonth.string is not None:
                #print('Current expiry month\'s URL is correct.')
                #print(potentialNextMonth['href'])
                urlSuffix=potentialNextMonth['href']
            else:
                currentEtfCompleted=True

        response=urllib.request.urlopen(urlBase+urlSuffix)
        soup=BeautifulSoup(response)
        mainTables=['dummy','dummy']
        superParentsOfMainTables=soup.findAll('table',{'class':'yfnc_datamodoutline1'})
        #maintd is used for referencing links to other expiry dates.
        maintd=soup.find('table',{'class':'yfnc_mod_table_title1'}).parent
        for i in range(2):
            mainTables[i]=superParentsOfMainTables[i].contents[0].contents[0].contents[0]
        
        tableIndex=0
        optionsResults=[]
        optionSymbol='dummy'
        optionType='dummy'
        last=0
        for tableIndex in range(2):
            tableLength=len(mainTables[tableIndex])
            for i in range(1,tableLength):
                #the loop starting on the above line is the loop iterating over all rows in the table.
                for j in range(8):
                    if j==0:
                        strike=float(mainTables[tableIndex].contents[i].contents[j].contents[0].string)
                    elif j==1:
                        optionSymbol=mainTables[tableIndex].contents[i].contents[j].contents[0].string
                        firstDigitPosition=search('\d',optionSymbol).start()
                        stockSymbol=optionSymbol[:firstDigitPosition]
                        #for most options, the option symbol will be len(stocksymbol)+14 characters long
                        #those are type 1 options.  However, some stocks have a second category of options
                        #(this category depends on the particular stock) with an extra 1 appended within
                        #the option symbol.  This becomes a type 2 option for this program's purposes.
                        #because of the extra character, characterBump is used to shift character pointers
                        #in the case of type 2 options.
                        if len(optionSymbol)==len(stockSymbol)+15:
                            #the option is a type 1 option in this case
                            specialType="type 1"
                            characterBump=0
                        elif len(optionSymbol)==len(stockSymbol)+16:
                            #the option is a type 2 option in this case
                            specialType="type 2"
                            characterBump=1
                        else:
                            print('option string not of the appropriate length.  quitting.')
                            quit()
                        expiryYear='20'+optionSymbol[firstDigitPosition+characterBump:firstDigitPosition+characterBump+2]
                        expiryMonth=optionSymbol[firstDigitPosition+characterBump+2:firstDigitPosition+characterBump+4]
                        expiryDay=optionSymbol[firstDigitPosition+characterBump+4:firstDigitPosition+characterBump+6]
                        expiryDate=date(int(expiryYear),int(expiryMonth),int(expiryDay))
                        if optionSymbol[firstDigitPosition+characterBump+6]=='C':
                            optionType='Call'
                        if optionSymbol[firstDigitPosition+characterBump+6]=='P':
                            optionType='Put'
                    elif j==2:
                        last=mainTables[tableIndex].contents[i].contents[j].contents[0].string#88888888888888888888888
                    elif j==3:
                        changeMagnitude=float(mainTables[tableIndex].contents[i].contents[j].contents[0].find('b').string)
                        #checks if there is a neg_arrow image in the daily change box.  if there is, say that changeSign is negative.
                        potentialNegativeArrowMarkup=mainTables[tableIndex].contents[i].contents[j].contents[0].find(attrs={'class':'neg_arrow'})
                        if potentialNegativeArrowMarkup is not None:
                            changeSign=-1
                        else:
                            changeSign=1
                        dailyValueChange=changeSign*changeMagnitude
                    #elif:  for getting the other columns in the table- not done yet
                        #dummy=4
                        
                appendedResults=[stockSymbol,optionSymbol, strike, expiryDate, optionType, last, dailyValueChange, specialType]
                #list of all things that should be appended into optionsresults:          
                #strike, optionSymbol, stockSymbol, expiryDate, optionType, last, dailyChangeValue, specialType
                optionsResults.append(appendedResults)
    #print(optionsResults)
    print('OptionsScraper has completed scraping.')
    return optionsResults

def scrapeLastUnderlyingPrice(symbol):
    #using stock symbol, gets last underlying price.
    urlBase='http://finance.yahoo.com/q?s='
    response=urllib.request.urlopen(urlBase+symbol)
    soup=BeautifulSoup(response)
    superParent=soup.find('span',{'class':'time_rtq_ticker'})
    forDate=superParent.parent.contents[4]
    date=forDate.contents[1].string
    print('------------------------')
    print(date)
    price=float(superParent.contents[0].string)
    return [price, date]
print(scrapeLastUnderlyingPrice("VXX"))
