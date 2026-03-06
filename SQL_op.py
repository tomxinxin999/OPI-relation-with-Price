import mysql.connector
import pandas as pd

##ets = pd.read_excel("E:\\Code_Python\\CZE\\DBoutput\\joindf.xlsx", header= 0)

cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
qur = ("CREATE TABLE mg401py AS "
        "select * from hd1 "
               "where  Contract like %s "
               "AND (L_Memb like %s or S_Memb like %s)")
cn = ('%RM401%',"摩根大通","摩根大通")

ce = ( "UPDATE mg401py "
       "SET LongPs = CASE WHEN L_Memb != %s THEN NULL ELSE LongPs END, "
       "ShortPs = CASE WHEN S_Memb != %s THEN NULL ELSE ShortPs END " )
en = ('摩根大通','摩根大通')

exp = ("SELECT * FROM mg401py "
       "INTO outfile 'E:/temp/mg401py.csv' character set GBK "
       "FIELDS terminated by ','  "
       "LINES terminated by '\r\n' " )
cursor.execute (exp)

cursor.execute (qur ,cn)
cursor.fetchall()

cursor.execute (ce ,en)
da = cursor.fetchall()

cursor.execute("select Date,Contract,L_Memb,LongPs,S_Memb,ShortPs from mg401")
mg401 = cursor.fetchall();
df401 = pd.DataFrame(mg401, columns=['Date', 'Contract', 'L_Memb', 'LongPs', 'S_Memb','ShortPs'])

cnx.commit()
##cursor.close()
##cnx.close()


##mysql> update leftjoin
##    -> SET LongPs = CASE WHEN L_Memb not like '%摩根大通%' THEN NULL ELSE LongPs END,
##    -> ShortPs = CASE WHEN S_Memb not like '%摩根大通%' THEN NULL ELSE ShortPs END;
