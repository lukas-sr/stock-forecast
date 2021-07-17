from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as pl

# Quotation for IBOVESPA index in the ibov_quotation dataframe 
# Data Frame columns ===> 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'
#
# web.DataReader('ticker', data_source='yahoo', start='mm/dd/yy', end='mm/dd/yy')
ibov_quotation = web.DataReader('^BVSP', data_source='yahoo', start='01-01-2020', end='07-17-2021')
print(ibov_quotation)

# display graph for the IBOVESPA index
ibov_quotation['Adj Close'].plot(figsize=(10,10))
pl.show()
