import xlrd
import pandas as pd
import numpy as np

df = pd.read_csv('C:\Users\Ishant\Desktop\BE Project\Combined_99Acres.csv')
# print df.head()
df2 = df.copy()
row = 1

for index in range(1,32794):
    try:
        if str(df2.at[row, 'Price']).find('Cr'):
            k = str(df2.at[row, 'Price']).replace('Cr', '')
            df2.at[row,'Price'] = k.replace(k,str(float(k)*100))

    except Exception as e:
        print e
    try:
        if str(df2.at[row,'Price per sq.Ft']).find(','):
            df2.at[row,'Price per sq.Ft'] = str(df2.at[row,'Price per sq.Ft']).replace(',','')
    except Exception as e:
        print ''
    row = row+1
df2.to_csv('C:\Users\Ishant\Desktop\Combined_99Acres.csv')
print df2.head()

# print df.head() #shows us the first 5 rows and headers

# print df.dtypes #This will return a list with your data types in it
# print df.shape #to know how many columns and rows are in our dataset
# print df.describe()

