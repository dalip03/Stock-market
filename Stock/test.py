from yahoo_fin.stock_info import *
import yahoo_fin.stock_info as si

# top_gainers = 	si.get_day_gainers(3)
# stockcode = list(top_gainers['Symbol'])
# Stocklist = ['TSLA','AAPL','BAC']
temp = (si.get_quote_data('TSLA'))
temp = temp['price']
print(temp)
