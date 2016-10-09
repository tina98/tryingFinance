import requests
import json
import csv
from yahoo_finance import Share
import time

stocks={}
with open('security-universe_20161008.csv') as csvfile:
	reader=csv.DictReader(csvfile)
	for row in reader:
		ticker=row['ticker']
		countryCode=row['countryCode']
		assetType=row['assetType']
		if assetType=="Stock":
			if stocks.has_key(countryCode):

				tempList=stocks[countryCode]
				tempList.append(ticker)
				stocks[countryCode]=tempList
			else:
				stocks[countryCode]=[ticker]

positions=""
print stocks

monthsAhead=input("How many months ahead would you to vacation? ")
listStocksWithNoYahoo=[]
for country in stocks:
	tempStock=""
	value=0
	listStocksWithNoYahoo=[]
	ticks=stocks[country]
	sumOfCompany=0
	for tick in ticks:

		try:
			tempStock=Share(tick)
			tempstock.refresh()
			print tempStock.get_price();
			value=float(tempStock.get_price())*int(tempStock.get_volume())
			sumOfCompany=float(sumOfCompany)+value
		except:
			listStocksWithNoYahoo.append(tick)
			print "hit"
	
	for ls in listStocksWithNoYahoo:
		print ls
		ticks.remove(ls)


	weights={}
	for tick in ticks:
		try:
			tempStock=Share(tick)
			weights[tick]=(float(tempStock.get_price())*float(tempStock.get_volume()))/float(sumOfCompany)
		except:
			print "shits fucked"
			#listStocksWithNoYahoo.append(tick)

	print len(ticks)
	for tick in ticks:
		positions=positions+str(tick)+"~"+str(weights[tick])+"|"
	print positions
	# portfolioAnalysisRequest = requests.get("https://test3.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : positions, 'calculateExpectedReturns' : 'true', 'average':'true','simStartDate': '20161008', 'simEndDate': '20161028', 'simLengthInMonths': monthsAhead})
	# data=json.loads(portfolioAnalysisRequest.text)
	# data=data['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['holdings']
	positions=""
	sumOfCompany=0
	listStocksWithNoYahoo=[]
	value=0



print "done"


