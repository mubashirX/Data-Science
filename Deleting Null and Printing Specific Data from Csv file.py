# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:56:55 2022

@author: Hp
"""

import pandas as pd
df=pd.read_csv("StudentMarkSheet.csv")
print(df)
df.info()

print("NUMBER OF ROWS IN THE DATAFRAME",len(df))
df=df.dropna(how='all')
x=len(df)
print("AFTER DROPING THE ROWN THAT CONTAIN All NULL VALUE = ",len(df))
df=df.dropna(how='any')
y=len(df)
print("AFTER DROPING THE ROWN THAT CONTAIN ANY NULL VALUE = ",len(df))
print("THE NUMBER OF ROWS THAT CONTAIN ANY NULL VALUE = ",x-y)


print(df[df['Student name']=='James Walker'])