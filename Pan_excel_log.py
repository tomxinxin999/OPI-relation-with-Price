import os
import pandas as pd
import xlrd
folder_ph = "C:\\Python_Code\\DataHold"
folder_ot = "C:\\Python_Code\\DataHold\opt"
##all_files = os.listdir(folder_ph)
##for file_name in all_files:
##      if file_name.endswith('.xlsx'):
####           file_ph = os.path.join(folder_ph, file_name)
##     df = pd.read_excel(file_ph)
##     dfs.append(df)

##combined_df = pd.concat(dfs, ignore_index=True)###5. Concatenate the DataFrames into a single DataFrame:


################# Process excel file data  #################
import pandas as pd
import xlrd
df = pd.read_excel("C:\\Python_Code\\DataHold\\FutureDataHoldingRM20230801.xls",header=None)
############## extract date and contract #################  
ctc1 = df.iloc[1,0].split("：")[1].split("   ")[0]
dateR = df.iloc[1,0].split("日期：")[1]
print (dateR)
print (ctc1)

##df = df.drop(columns=['Date']) #delete column
##df.iloc[1:21,1:10]
##df.loc[4:20]
##x.iloc[1] = {'x': 9, 'y': 99}
##df.index.stop-1
###############################
##df2.drop(index=[159], inplace=True)
##row_totals = df.sum(axis=1)
##column_totals = df.sum(axis=0)
##df.drop([0],axis=0)
##df.reset_index(drop=True, inplace=True)reset the index of a pandas DataFrame to match the position number

#########################  insert date and contract  #########################
df.insert(0, 'Contract', ctc1)
df.insert(0, 'Date', dateR)

k=16
while k<(df.index.stop-1)  :
    if df.iloc[k,2] != '合计':
        k += 1
    else:
        ctm = df.iloc[k+1,2].split("：")[1].split("   日")[0]
        fg= k + 3
        while df.iloc[fg,2]!='合计':
            df.iloc[fg,1] = ctm
            fg += 1
            if(fg==df.index.stop-1):
                break
        k=fg-1

##df.to_excel("c:\\to_non.xlsx",index = False, header = None)
df.loc[2]=['Date','Contract','No', 'Member1', 'Volume' , 'Vol_Change' , 'Member2' , 'LongPs' , 'L_Change', 'Member3' ,'ShortPs' , 'S_Change']

df.drop([0,1],axis=0,inplace=True) # delete the first two row
df.rename(columns=df.iloc[0],inplace=True)  # re-assign new header to the dataframe
df.drop(index=2,axis=0, inplace=True )     #delete row 
print (df.head(1))
###### Find rows with "合计" in the "名次" column  ##########
e = df.index.stop -1 
hjr = df[df['No'] == '合计'].index
########  Delete the rows and the two rows immediately under them  ##########
df.drop(hjr, inplace=True)
for m in hjr:
    if (m <= e-3):
        df.drop(m + 1, inplace=True)
        df.drop(m + 2, inplace=True)
        
df.to_excel("C:\\Python_Code\\DataHold\\opt\\RM2023-08-01.xlsx",index = False)
##df.reset_index(drop=True, inplace=True)

############### mySql #################








