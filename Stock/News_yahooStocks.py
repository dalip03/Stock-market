from yahoo_fin import news

def yahooNews():
    stocks = ['TSLA','AAPL','AMZN','NVDA','NIO']
    # stocks = ['TSLA','AAPL']
    
    allNews = []
    for i in stocks:
        scraped_news = ''
        temp = news.get_yf_rss(i)
        temp2 = [temp[0]][0]
        b= temp2['summary'].split(".")[0]
        b = b+'.'
        

        if (len(b)<120):
            b=b+ temp2['summary'].split(".")[1]
            b = b+'.'
            scraped_news= scraped_news+(b)
        else:
            scraped_news= scraped_news+(b)

        allNews.append(scraped_news)
    return allNews
# temp = yahooNews()
# print(temp)
# for i in temp:
#     print((i))