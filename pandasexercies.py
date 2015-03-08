import pandas as pd
import numpy as np
import matplotlib as plt

#f open = ('DataMiner.csv','r')

#df.to_excel('DataMiner.csv', sheet_name='DataMiner') 
#df.to_csv('DataMiner.csv')
#pd.read_csv('DataMiner.csv')


#1
#print(open('DataMiner.csv').read())
#2
#print pd.read_csv('DataMiner.csv')
#3
print pd.read_csv('DataMiner.csv', index_col=['Pais','Porcentaje'])
