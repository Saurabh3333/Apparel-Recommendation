import pandas as pd

recomendations=pd.DataFrame()
df=pd.read_excel('test.xlsx')
df=df.astype(str)
df=df.set_index('Объект').T
df.to_excel('DataSet.xlsx')
df=pd.read_excel('DataSet.xlsx',index_col=0)
recList=list()
