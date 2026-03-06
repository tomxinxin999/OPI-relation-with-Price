import mysql.connector
import pandas as pd
import numpy as np

cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
##dts.to_excel("E:\\Code_Czce\\DataHold\\tem.xlsx",index=False)

dts = pd.read_excel("E:\\Code_Python\\CZE\\datahold\\opt\RM2023-07-31.xlsx", header=0)
columns_kma = ['Volume', 'Vol_Change', 'LongPs', 'L_Change', 'ShortPs', 'S_Change']
for column in columns_kma:
    dts[column] = dts[column].str.replace(',', '')

##dts = pd.read_excel("C:\\Python_Code\\DataHold\\opt\\RM2023-07-31.xlsx",header=0)
##dts = dts.replace('-', np.nan)
dts = dts.replace('-', 0)

addrow = ("INSERT INTO hd1 "
"(Date,Contract, No, Member1, Volume, Vol_Change, Member2, LongPs, L_Change, Member3, ShortPs, S_Change) "
"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )")    

for  row in dts.to_numpy():
    values = tuple(row)
    cursor.execute(addrow, values)

cnx.commit()

cursor.close()
cnx.close()
