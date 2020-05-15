# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:25:49 2020

@author: yly
"""
#input a positive number
k= input("please import an integer less than 8192:")
t=eval(k)
#convert to binary
a=bin(t)
#take out"0b"
b=a[2:]
#break b up into list
c=list(b)
n=''
for i in range(len(c)):
    c[i]=int(c[i])
    if c[i]==1:
        n+=str(2)+'**'+str(len(c)-i-1)+'+'#To delete "+" existing at the end
        i+=1
    else:
        continue
print(n[:-1])#To delete "+" existing at the end
