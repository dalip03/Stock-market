
import yahoo_fin.stock_info as si
import pandas as pd

#  Symbol Name  Price (Intraday)




# top_gain_stocksCode = []


# top_gain_symbol.append(top_gainers['Symbol'])
# top_gain_name.append(top_gainers['Name'])
# top_gain_price.append(top_gainers['Price (Intraday)'])
# print(top_gain_symbol, top_gain_name)

# for i in range(len(top_gain_price)):
#     print(top_gain_symbol[i] , top_gain_name[i],  end="")


# top_gain_stocksCode.append((top_gainers['Symbol']))
# stockCode = []
# res = ""


# print(len(top_gain_stocksCode))
# for stk in top_gain_stocksCode:
 
#     stk= str(stk)
#     print(stk)
#     res = "".join(stk.split())
#     res = res[1:]
#     # stockCode.append(res[1:])
#     print(res)
    
# print(stockCode)
def topLoseData():   
    top_gainers = 	si.get_day_gainers(3)
    stockcode = list(top_gainers['Symbol'])

    top_stock_data = []
    # print(top_gain_stocksCode)


    for i in stockcode:
        temp = (si.get_quote_data(i))
        temp = temp['price']

        top_stock_data.append([temp['symbol'],
                    temp['regularMarketPrice']['fmt'],
                    temp['regularMarketDayHigh']['fmt'],
                    temp['regularMarketDayLow']['fmt']])

    # print(top_stock_data)

    # top_stock_data = ['a','b','c']

    # losers
    day_losers = 	si.get_day_losers()[0:3]
    stockcode = list(day_losers['Symbol'])


    lose_stock_data = []
    # print(top_gain_stocksCode)


    for i in stockcode:
        temp = (si.get_quote_data(i))
        temp = temp['price']

        lose_stock_data.append([temp['symbol'],
                    temp['regularMarketPrice']['fmt'],
                    temp['regularMarketDayHigh']['fmt'],
                    temp['regularMarketDayLow']['fmt']])
    # print(lose_stock_data)      


    columns_top_table = ['Code',
                   'Reg. Market Price',
                   'Reg. Market Day High',
                   'Reg. Market Day Low']
    return top_stock_data , lose_stock_data, columns_top_table