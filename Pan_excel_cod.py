import os
import pandas as pd
import xlrd


def clear_file (f_path,outfolder):
    ##f_path = "E:\\Code_Python\\CZE\\FutureDataHoldingRM20230731.xls"
    df = pd.read_excel(f_path,header=None)
    ctc1 = df.iloc[1,0].split("：")[1].split("   ")[0]  
    dateR = df.iloc[1,0].split("日期：")[1]
    df.insert(0, 'Contract', ctc1) ## new contract column
    df.insert(0, 'Date', dateR)    ## new Date column

    print (dateR)
    print (ctc1)


    ############### update contract column ############
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
    df.loc[2]=['Date','Contract','No', 'Vol_Memb', 'Volume' , 'Vol_Change' , 'L_Memb' , 'LongPs' , 'L_Change', 'S_Memb' ,'ShortPs' , 'S_Change']
    ################## create new header  #########
    df.drop([0,1],axis=0,inplace=True)
    df.rename(columns=df.iloc[0],inplace=True)
    df.drop(index=2,axis=0, inplace=True )
    ##################  delete heji  #########
    e = df.index.stop -1 
    hjr = df[df['No'] == '合计'].index
    df.drop(hjr, inplace=True)
    for m in hjr:
        if (m <= e-3):
            df.drop(m + 1, inplace=True)
            df.drop(m + 2, inplace=True)

    outname = "RM"+dateR+".xlsx"
##    outfolder = "C:\\Python_Code\\DataHold\\opt"
    out_path = os.path.join(outfolder, outname)
    df.to_excel(out_path,index = False)

############ Main ##########

folder_ph = "E:\\Code_Python\\CZE\\DataHold"
outfolder = "E:\\Code_Python\\CZE\\DataHold\\opt"
all_files = os.listdir(folder_ph)
for fe in all_files:
    f_path = os.path.join(folder_ph, fe)
    clear_file (f_path,outfolder)
