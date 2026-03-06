import mysql.connector
import pandas as pd

ets = pd.read_excel("E:\\Code_Python\\CZE\\DBoutput\\joindf.xlsx", header= 0)

cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
addrow = ("INSERT INTO leftjoin"
	  "(Date, Open, High, Low, Close, OPI, L_Memb, LongPs, S_Memb, ShortPs) "
	  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s )")

for  row in ets.to_numpy():
	values = tuple(row)
	cursor.execute(addrow, values)

	

cnx.commit()
cursor.close()
cnx.close()


##mysql> update leftjoin
##    -> SET LongPs = CASE WHEN L_Memb not like '%摩根大通%' THEN NULL ELSE LongPs END,
##    -> ShortPs = CASE WHEN S_Memb not like '%摩根大通%' THEN NULL ELSE ShortPs END;
