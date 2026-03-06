import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
cursor.execute("select date,contract,L_Memb,LongPs,S_Memb,ShortPs "
	       "FROM hd1 "
	        "WHERE date = '2023-09-12' AND contract like '%RM401%' AND (L_Memb LIKE '%摩根%' OR S_Memb LIKE '%摩根%') "
               )
row = cursor.fetchall()
rf =  pd.DataFrame(row, columns=['Date', 'Contract', 'L_Memb', 'LongPs','S_Memb', 'ShortPs'])
rf.loc[rf['L_Memb'] != '摩根大通', 'LongPs'] = None
rf.loc[rf['S_Memb'] != '摩根大通', 'ShortPs'] = None
rf.to_excel("e:\\Temp\\rt_file.xlsx", index = False )
print ("Already create a rt_file.xlsx file")
cursor.close()
cnx.close()
