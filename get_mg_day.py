import pandas as pd
import mysql.connector

##Lfn = input ("\nInput the left filename")


cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
cursor.execute("select date,contract,L_Memb,LongPs,S_Memb,ShortPs "
	       "FROM hd1 "
               "WHERE date = '2023-09-19' AND contract like '%RM401%' AND (L_Memb LIKE '%摩根%' OR S_Memb LIKE '%摩根%') " )
row = cursor.fetchall()


print (row)
cursor.close()
cnx.close()
