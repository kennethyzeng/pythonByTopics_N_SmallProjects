#1 Installation
pip install pandas   or conda install pandas

import pandas as pd 
import numpy as np 
data = pd.read_csv('http://hilpisch.com/tr_eikon_eod_data.csv',
                   index_col=0, parse_dates=True)
#
data = pd.DataFrame(data['AAPL.O'])
print(data.shift())  #The data of that column shit one position down 
print(data.shift(6))  ##The data of that column shit six position down 