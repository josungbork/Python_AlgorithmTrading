import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Get kakao data from google
kakao = web.DataReader('KRX:035720', 'google', '2016-01-01', '2018-03-08')


# Moving average
ma5 = kakao['Close'].rolling(window=5).mean()
ma20 = kakao['Close'].rolling(window=20).mean()
ma60 = kakao['Close'].rolling(window=60).mean()
ma120 = kakao['Close'].rolling(window=120).mean()

#print(kakao.tail(10))
# Insert columns
kakao.insert(len(kakao.columns), "MA5", ma5)
kakao.insert(len(kakao.columns), "MA20", ma20)
kakao.insert(len(kakao.columns), "MA60", ma60)
kakao.insert(len(kakao.columns), "MA120", ma120)

# Plot
plt.plot(kakao.index, kakao['Close'], label='Close')
plt.plot(kakao.index, kakao['MA5'], label='MA5')
plt.plot(kakao.index, kakao['MA20'], label='MA20')
plt.plot(kakao.index, kakao['MA60'], label='MA60')
plt.plot(kakao.index, kakao['MA120'], label='MA120')

plt.legend(loc="best")
plt.grid()
plt.show()