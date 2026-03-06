import pandas as pd
import mysql.connector
cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
cursor.execute("SELECT Date,open, high, low, close, close_oi,Contract, L_Memb, LongPs, L_Change FROM hd1 WHERE L_Memb  like '%摩根大通%' ")
da = cursor.fetchall()
dtin = pd.DataFrame(da, columns=['Date', 'Contract', 'L_Memb', 'LongPs', 'L_Change'])
cursor.close()
cnx.close()



sqlquery = "SELECT * FROM plot"
cursor.execute(sqlquery)
rows =cursor.fetchall()
col_name = pd.DataFrame(rows, columns=['Date', 'Open', 'High', 'Low', 'Close' , 'Close_oi', 'Contract','L_Memb',  'LongPs', 'L_Change', 'S_Memb', 'ShortPs', 'S_Change'])
