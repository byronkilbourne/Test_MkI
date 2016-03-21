import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
import datetime as dt

def bytespdate2num(fmt, encoding ='utf-8'):
	strconverter = mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s = b.decode(encoding)
		return strconverter(s)
	return bytesconverter
	
def graph_data(stock):
	stock_price_url = 'https://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
	source_code = urllib.request.urlopen(stock_price_url).read().decode()
	stock_data = []
	split_source=source_code.split('\n')
	for line in split_source:
		split_line = line.split(',')
		if len(split_line) == 6:
			if 'values' not in line and 'labels' not in line:
				stock_data.append(line)
				
#	date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,delimiter=',',unpack=True,converters={0:bytespdate2num('%Y%m%d')})
	date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,delimiter=',',unpack=True)
	dateconv = np.vectorize(dt.datetime.fromtimestamp)
	date = dateconv(date)
	
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1),(0,0))
	
	ax1.plot_date(date, closep,'-',label='Price')
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	ax1.grid(True)
	
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Interesting Graph\nCheck it out')
	plt.subplots_adjust(left=0.09,bottom=0.2,right=0.94,top=0.90,wspace=0.05,hspace=0.05)
	plt.legend()
	plt.show()
	
graph_data('MSFT')
