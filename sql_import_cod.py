import mysql.connector
import pandas as pd
import numpy as np
import os

def tomysql(f_path):
    ##dts.to_excel("E:\\Code_Czce\\DataHold\\tem.xlsx",index=False)

    dts = pd.read_excel(f_path, header=0)
    columns_kma = ['Volume', 'Vol_Change', 'LongPs', 'L_Change', 'ShortPs', 'S_Change']
    for column in columns_kma:
        dts[column] = dts[column].str.replace(',', '')    ###  delete all commas

    ##dts = pd.read_excel("C:\\Python_Code\\DataHold\\opt\\RM2023-07-31.xlsx",header=0)
    ##dts = dts.replace('-', np.nan)
    dts = dts.replace('-', 0)

    addrow = ("INSERT INTO hd1 "
    "(Date,Contract, No, Vol_Memb, Volume, Vol_Change, L_Memb, LongPs, L_Change, S_Memb, ShortPs, S_Change) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )")    

    for  row in dts.to_numpy():
        values = tuple(row)
        cursor.execute(addrow, values)
################# main  ######################
        
cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
outfolder = "E:\\Code_Python\\CZE\\DataHold\\opt"
all_expo_excels = os.listdir(outfolder)
for fe in all_expo_excels:
    f_path = os.path.join(outfolder, fe)
    print(f_path)
    tomysql(f_path)
cnx.commit()

cursor.close()
cnx.close()
