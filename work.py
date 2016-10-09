import requests
import json
import csv
import quandl
import time

quandl.ApiConfig.api_key="D_ojfxbH-PuJ4ef2bEok"
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
	positions=""
	nameStock=""
	tempStock=""
	value=0
	listStocksWithNoYahoo=[]
	ticks=stocks[country]
	sumOfCompany=0
	for tick in ticks:

		try:
			nameStock="WIKI/"+tick.upper()
			print "why"
			tempStock=quandl.get(nameStock,rows=1)
			print "doesn't"
			tempStock=tempStock.to_csv()
			print "this"
			reader2=csv.DictReader(tempStock)
			for row2 in reader2:
				print(row['Open'])
				value=float(row['Open'])*float(row['Volume'])
			sumOfCompany=float(sumOfCompany)+value
		except:
			listStocksWithNoYahoo.append(tick)
			print "hit"
	
	for ls in listStocksWithNoYahoo:
		ticks.remove(ls)

	weights={}
	for tick in ticks:
		try:
			tempStock=json.loads(json.dumps(getQuotes(tick)))[0]
			weights[tick]=tempStock[LastTradePrice]/float(sumOfCompany)
		except:
			print "shits fucked"
			#listStocksWithNoYahoo.append(tick)

	for tick in ticks:
		positions=positions+str(tick)+"~"+str(weights[tick])+"|"
		print "positions"
	print positions
	# portfolioAnalysisRequest = requests.get("https://test3.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : positions, 'calculateExpectedReturns' : 'true', 'average':'true','simStartDate': '20161008', 'simEndDate': '20161028', 'simLengthInMonths': monthsAhead})
	# data=json.loads(portfolioAnalysisRequest.text)
	# data=data['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['holdings']
	positions=""
	sumOfCompany=0
	listStocksWithNoYahoo=[]
	value=0



print "done"


