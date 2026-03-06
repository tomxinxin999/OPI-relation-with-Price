#import mysql.connector
import pandas as pd
from tqsdk import TqApi, TqAuth

######  download kindle lines  ############
api = TqApi( auth=TqAuth("13910926112", "riit1234"))
kdline  = api.get_kline_serial("CZCE.RM401", 24*60*60)
ixkn = api.get_kline_serial("KQ.i@CZCE.RM", 24*60*60)
################  KQ.i@SHFE.bu - 上期所bu品种指数#########
######  Clear data  ############
kd = kdline.copy()
dte = pd.to_datetime(kd['datetime']) + pd.to_timedelta(1, unit='d') ###  chang nanoseconds and push one day forward
kd['Date'] = dte.dt.strftime('%Y-%m-%d') ## create new column Date

kd = kd[(kd['datetime'] != 0)]
kd = kd.reset_index(drop=True)  # reset row index start from 0
kd.drop(['datetime','id','open_oi','duration'],axis=1, inplace=True)
cols = ['Date']  + [col for col in kd if col != 'Date']
kd = kd [cols]
print("\nFinished clear RM401 candle lines data in Pandas")
print (kd)
##pk['Date'] = pk['Date'].shift(-1)
cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
addrow = ("INSERT IGNORE INTO kdLineRM401"
	  "(Date, open, high, low, close, volume, close_oi, symbol) "
	  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s )")

for  row in kd.to_numpy():
	values = tuple(row)
	cursor.execute(addrow, values)
cursor.execute("delete from kdlinerm401 where date < '2023-03-03'")
cnx.commit()
print("\nFinished created a table -- kdlineRM401 in mySQL")  ####
##################  begain to clear RM index candle lines data ##########
pk = ixkn 
kn = pd.to_datetime(ixkn['datetime']) + pd.to_timedelta(1, unit='d') ###  chang nanoseconds to readable format
pk['Date'] = kn.dt.strftime('%Y-%m-%d') ## create new Date column 
pk.drop(['datetime','id','open_oi','duration'],axis=1, inplace=True)

cols = ['Date']  + ['close_oi']
pk = pk [cols]
##pk['Date'] = pk['Date'].shift(-1)
print (pk)
print("\nFinished clear RM Index candle lines data in Pandas")
cnx = mysql.connector.connect(user='root', password='riit1234',host='localhost',database='datahold')
cursor = cnx.cursor()
addrow = ("INSERT IGNORE ixopi"
	  "(Date, ixopi) "
	  "VALUES ( %s, %s )")

for  row in pk.to_numpy():
	values = tuple(row)
	cursor.execute(addrow, values)
	
cursor.execute("delete from ixopi where date < '2023-03-03'")
print("\nFinished created a table -- ixopi in mySQL")
cnx.commit()
cursor.close()
cnx.close()
