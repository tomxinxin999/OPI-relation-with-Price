import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
cursor.execute("UPDATE  kdlinerm401 "
               "JOIN ixopi on kdlinerm401.date = ixopi.date "
	       "SET kdlinerm401.close_oi = ixopi.ixopi; "
                )

##joindf.to_excel("e:\\Temp\\kd.xlsx", index = False )
print ("Already create a .xlsx file")
cursor.close()
cnx.close()
