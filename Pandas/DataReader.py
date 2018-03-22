import pandas_datareader.data as web
import datetime

start = datetime.datetime(2018, 2, 26)
end = datetime.datetime(2018, 3, 4)
#samsung = web.DataReader('KRX: 005930', 'google', start, end)

kakao = web.DataReader('KRX:035720', 'google', start, end)
#print(samsung)
print('\n')
print(kakao)
