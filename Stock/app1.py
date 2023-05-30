# importing the libraries
from flask import Flask,render_template,request

from tableStocks import tabledata
import pandas as pd
from TopLoserStocks import topLoseData
import numpy as np
from News_yahooStocks import yahooNews
import time

import threading 
#Global variables

app=Flask(__name__)

# temp = stockdata(['AAPL','META'])
# print(temp)
#user defined routes


@app.route("/", methods=["GET" ,"POST" ])
def home1():   
    
    gain, lose ,gainlosehead =  topLoseData()
    news = yahooNews()
    return render_template('indexjs.html',gain=gain, lose= lose ,gainlosehead = gainlosehead, news = news)

@app.route("/table", methods=["GET" ,"POST" ])
def home2():   
    while True:
        # time.sleep(2000)
        context,tablehead =  tabledata()
        return render_template('table.html', context =context , tablehead= tablehead) 
# ,tablehead = tablehead)




# @app.route("/prediction",methods=['GET','POST'])
# def predict():
#     output = pre(list(df['text']))
#     df['ouput'] = output
#     context = df
#     return render_template('prediction.html',tables=context)



if __name__ =='__main__':
    app.run(debug=True      )       


