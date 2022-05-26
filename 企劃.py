#!/usr/bin/env python
# coding: utf-8

# In[2]:


#處理基本面 抓出健康的股票
import locale
import csv
combine = []
asset = []
stock = []
num = 0
#asset[i][7]是資產總額 
#combine[i][17]是稅前淨利
#combine[i][18]是利息費用 
with open('111第一季 資產負債表.csv', encoding='big5' , errors = 'ignore') as a1:
    rows = csv.reader(a1, delimiter=',')
    asset += rows
with open('111第一季 綜合損益表.csv', encoding='big5' , errors = 'ignore') as a2:
    rows = csv.reader(a2, delimiter=',')
    combine += rows
    for i in range(1,921):
        errors = 'ignore'
        if combine[i][17]=='--' or combine[i][18]=='--' or combine[i][5]=='--' or locale.atof(combine[i][5])==0:
            continue
        #稅後純益/營業收入 = 獲利能力
        elif (locale.atof(combine[i][17])-locale.atof(combine[i][18]))/locale.atof(combine[i][5]) >= 0.2:
            #營業收入/總資產 = 資產運用能力 
            if (locale.atof(combine[i][5])/locale.atof(asset[i][7])) >= 0.01:
                num += 1
                ##print(asset[i][3],asset[i][4])
                stock.append(asset[i][3])
print(stock)


# In[ ]:





# In[ ]:





# In[3]:


#自營商在前一月的買賣超
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import requests
import pandas as pd
import numpy as np
import csv
from io import StringIO
bigdata=[]
faren = []
# 載股價
r = requests.post('https://www.twse.com.tw/fund/TWT54U?response=csv&date=20220516&selectType=ALLBUT0999')
df = csv.reader(StringIO(r.text.replace("=", "")))
bigdata += df
for i in range(2,len(bigdata)-10):
    if float(bigdata[i][4].replace(',','')) >= 0:
        if float(bigdata[i][10].replace(',','')) >= 0:
            faren.append(bigdata[i][0])
print(faren)


# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


record = []
for i in stock:
    for j in faren:
        if i == j :
            record.append(i)
            print(i)
        else :
            continue


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


import pandas as pd
import pandas_datareader.data as pdr
import datetime
from datetime import date
import time

#處理日期 
today = datetime.date(2022,5, 24)
lm = datetime.timedelta(days=-90)
print(today+lm)

for j in record:
    stockname = str(j)
    print(j)
    df=pdr.DataReader(stockname+'.tw','yahoo','2022-03-31',today)
    close=df['Close'][today+lm:today]
    sma10=close.rolling(10).mean()
    sma20=close.rolling(20).mean()
    sma60=close.rolling(60).mean()
    if close[35]>=50:
        continue
    else:
        print(close)
        for i in range(0,len(close)):
            if close[i]>=sma10[i]:
                print(i,close[i],'buy')
    time.sleep(1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




