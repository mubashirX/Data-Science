# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 00:30:02 2022

@author: Hp
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("StudentMarkSheet.csv")
df=df.dropna(how='any')


avgbio=df[df["Exam name"]=="Biology"]
print(avgbio)
avgbio=avgbio["Marks"]
avgbio=(avgbio.sum())/(len(avgbio))
print("THE AVERAGE OF BIOLOGY MARKS IS = ",avgbio)


avgchem=df[df["Exam name"]=="Chemistry"]
print(avgchem)
avgchem=avgchem["Marks"]
avgchem=(avgchem.sum())/(len(avgchem))
print("THE AVERAGE OF CHEMISTRY MARKS IS = ",avgchem)


avgmath=df[df["Exam name"]=="Mathematics"]
print(avgmath)
avgmath=avgmath["Marks"]
avgmath=(avgmath.sum())/(len(avgmath))
print("THE AVERAGE OF MATHEMATICS MARKS IS = ",avgmath)


avgphil=df[df["Exam name"]=="Philosophy"]
print(avgphil)
avgphil=avgphil["Marks"]
avgphil=(avgphil.sum())/(len(avgphil))
print("THE AVERAGE OF PHILOSOPHY MARKS IS = ",avgphil)


avgphs=df[df["Exam name"]=="Physics"]
print(avgphs)
avgphs=avgphs["Marks"]
avgphs=(avgphs.sum())/(len(avgphs))
print("THE AVERAGE OF PHYSICS MARKS IS = ",avgphs)


avgsoc=df[df["Exam name"]=="Sociology"]
print(avgsoc)
avgsoc=avgsoc["Marks"]
avgsoc=(avgsoc.sum())/(len(avgsoc))
print("THE AVERAGE OF PHILOSOPHY MARKS IS = ",avgsoc)

subject=["BIO","CHEM","PHYS","SOCIO","MATHE","PHIL"]
average=[avgbio,avgchem,avgphs,avgsoc,avgmath,avgphil]
plt.bar(subject,average,fc="blue")
plt.show()
