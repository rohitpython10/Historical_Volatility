#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import statistics as st
import math 

historicalrange= 30


#import file
df= pd.read_csv("a50-historical.csv")

#convert dates to date format
date_df= df['Date'].tolist()
dates=[]
for d in date_df:
    temp= datetime.datetime.strptime(d,'%b %d, %Y')
    dates.append(temp)

#convert strings to numbers
price_df= df['Price'].tolist()
prices=[]
for p in price_df:
    temp= float (p.replace(',',''))
    prices.append(temp)

#calculate interday returns
interdayresults= []
for i in range(len(prices)-1):
    temp= (prices [i]/prices[i+1]-1)
    interdayresults.append(temp)

#calculate volatility
volatility= []
for i in range(historicalrange, len(interdayresults)):
    temp= st.stdev(interdayresults[i-historicalrange:i])
    volatility.append (temp)

#calculate historical volatility
historicalvolatility= []
for i in volatility:
    temp= i * math.sqrt(252)
    historicalvolatility.append (temp)

#plotting values
fig, ax1= plt.subplots()
ax2= ax1.twinx()
ax1.plot(dates[historicalrange+1:], historicalvolatility, 'g-')
ax2.plot(dates[historicalrange+1:], prices[historicalrange+1:])
plt.show()

                          

