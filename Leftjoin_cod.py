import pandas as pd
import mysql.connector


cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
cursor.execute("select kdlinerm401.date as date,"
	       "hd1.Contract, kdlinerm401.open, kdlinerm401.high, kdlinerm401.low, kdlinerm401.close, kdlinerm401.close_oi, hd1.L_Memb, hd1.LongPs, hd1.S_Memb, hd1.ShortPs "
	       "FROM kdlinerm401 "
	       "LEFT JOIN ( SELECT date,Contract,L_Memb,LongPs,S_Memb,ShortPs  FROM hd1 "
               " WHERE hd1.Contract like '%RM401%' AND (hd1.L_Memb LIKE '%摩根大通%' OR hd1.S_Memb LIKE '%摩根大通%' )) "
               "AS hd1 ON kdlinerm401.date = hd1.date "
               "WHERE kdlinerm401.date > '2023-03-20' " )
##cnx.commit ()
row = cursor.fetchall()
joindf =  pd.DataFrame(row, columns=['Date', 'Contract',  'Open', 'High', 'Low', 'Close' ,'OPI','L_Memb', 'LongPs','S_Memb', 'ShortPs'])
joindf.loc[joindf['L_Memb'] != '摩根大通', 'LongPs'] = None
joindf.loc[joindf['S_Memb'] != '摩根大通', 'ShortPs'] = None
joindf.to_excel("e:\\Temp\\joinRM.xlsx", index = False )
print ("Already create a joindf.xlsx file")
cursor.close()
cnx.close()


##SELECT DISTINCT kdlinerm309.date, hd1.Contract,kdlinerm309.open, kdlinerm309.high, kdlinerm309.low, kdlinerm309.close, kdlinerm309.close_oi,
##    hd1.L_Memb, hd1.LongPs, hd1.S_Memb, hd1.ShortPs
##FROM kdlinerm309
##LEFT JOIN hd1 ON kdlinerm309.date = hd1.date
##WHERE hd1.Contract LIKE '%RM309%' AND (hd1.L_Memb LIKE '%摩根大通%' OR hd1.S_Memb LIKE '%摩根大通%');
##
############### Important  LeftJoin SQL  statement #######
##select kdlinerm401.date as date,
##hd1.Contract, kdlinerm401.open, kdlinerm401.high, kdlinerm401.low, kdlinerm401.close, kdlinerm401.close_oi,hd1.L_Memb, hd1.LongPs, hd1.S_Memb, hd1.ShortPs
##FROM kdlinerm401
##LEFT JOIN ( SELECT date,Contract,L_Memb,LongPs,S_Memb,ShortPs  FROM hd1
##WHERE hd1.Contract like '%RM401%' AND (hd1.L_Memb LIKE '%摩根大通%' OR hd1.S_Memb LIKE '%摩根大通%' ))
##AS hd1 ON kdlinerm401.date = hd1.date
##WHERE kdlinerm401.date > '2023-06-06';
