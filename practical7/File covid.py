# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:18:46 2020

@author: yly
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#importing the .csv ﬁle works 
os.chdir(r"C:\Users\yly\desktop\IBI\IBI1_2019-20\practical7")
#showing all rows, and every third column between (and including) 0 and 15
covid_data=pd.read_csv("full_data.csv")
print(covid_data.iloc[:,0:16:3])
#used a Boolean to show “total cases” for all rows corresponding to Afghanistan
my_columns_1 = [False, True, False, False, True,False] 
b= covid_data.iloc[:,my_columns_1]
a=b.values
for i in range(len(b)):
    if a[i,0] == 'Afghanistan':
        print(a[i,1])
    else:
        continue
#computed the mean and median of new cases for the entire world
#created a boxplot of new cases worldwide    
my_columns_2 = [True, True, True, True, False,False] 
c= covid_data.iloc[:,my_columns_2]
d=c.values
list_1=[]
list_2=[]
list_3=[]
for i in range(len(b)):
    if d[i,1] == 'World':
        list_1.append(d[i,2])
        list_2.append(d[i,0])
        list_3.append(d[i,3])
    else:
        continue
wnc=np.array(list_1) #wnc=world new cases
c=np.mean(wnc)
d=np.median(wnc)
print(c)
print(d)
wd=np.array(list_2)  #wd=world date
wnd=np.array(list_3)  #wnd=world new deaths
score=wnc
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True,meanline=False)
plt.title("a boxplot of new cases worldwide")
plt.ylabel("new cases")
plt.show()
#plotted both new cases and new deaths worldwide
plt.figure(figsize=(8,3),dpi=80)
x_1=wd
x_2=wd
y_1=wnc
y_2=wnd
plt.plot(x_1,y_1,label='world new cases',color='#00008B',linestyle='-',linewidth=3)
plt.plot(x_2,y_2,label='world new deaths',color='tomato',linestyle=':',linewidth=3)
plt.legend(loc='upper left')
_x=list_2[::3]
plt.xticks(_x,rotation=-90)
plt.xlabel("date")
plt.ylabel("numbers")
plt.title("a boxplot of both new cases and new deaths worldwide")
plt.grid(alpha=0.2)
plt.show()
#There is the code to answer the question in txt
my_columns_3 = [True, True, False, False, True, True] 
e= covid_data.iloc[:,my_columns_3]
f=e.values
list_4=[]
list_5=[]
list_6=[]
list_7=[]
list_8=[]
list_9=[]
for i in range(len(e)):
    if f[i,1] == 'Germany':
        list_4.append(f[i,2])
        list_5.append(f[i,3])
        list_6.append(f[i,0])
    else:
        continue
for i in range(len(e)):
    if f[i,1] == 'United Kingdom':
        list_7.append(f[i,2])
        list_8.append(f[i,3])
        list_9.append(f[i,0])
    else:
        continue
Gt=np.array(list_4)
Gd=np.array(list_5)
Et=np.array(list_7)
Ed=np.array(list_8)
Gdr=Gd/Gt
Edr=Ed/Et
for i in range(len(Gt)):
    if Gt[i]==0:
        Gt[i]=1
for i in range(len(Et)):
    if Et[i]==0:
        Et[i]=1
Gdate=np.array(list_6)
Edate=np.array(list_9)
plt.figure(figsize=(8,3),dpi=80)
x__1= Gdate
x__2= Edate
y__1= Gdr
y__2= Edr
plt.plot(Gdate,Gdr,label='Germany',color='#00008B',linestyle='-',linewidth=3)
plt.plot(Edate,Edr,label='UK',color='tomato',linestyle=':',linewidth=3)
plt.legend(loc='center')
_x1=list_6[::3]
plt.xticks(_x1,rotation=-90)
_x2=list_9[::3]
plt.xticks(_x2,rotation=-90)
plt.xlabel("date")
plt.ylabel("numbers")
plt.title("a boxplot of the proportion of cases have died in Germany and UK")
plt.grid(alpha=0.2)
plt.show()
