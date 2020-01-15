#To Read cvs file   
import pandas as pd

# Read cvs file.
data = pd.read_csv('store.csv',header=None)#put the cvs file(Excel file)  here 

# data [['MILK','Bread'] , ['TEA','JAM'], ...] 
t = []
for i in range(0,len(data)):
    t.append(str(data.values[i][0]).split(","))#


from apyori import apriori

result = list(apriori(t,min_support=0.01,min_confidence=0.2,min_lift=3))


for i in range(0,len(result)):
    print(result[i].items)
