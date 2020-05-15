# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:42:30 2020

@author: yly
"""
##4.1some simple math
a=654
b=654654
c=b%7
if c==0:
    print ("b can be divided by 7")
else:
    print("b can not be divided by 7")
d=c/11
e=c/13
if a>e:
    print ("a is greater than e")
elif a>e:
    print ("e is greater than a")
else:
    print ("a and e are equal")
    
##4.2booleans
#giving booleans variable x and y, calculate the value of z
x=True
y=False
z=(x and not y)or(y and not x) 
w=(x!=y)
#print z and w to verify the consistence of them
if z==w:
    print("w and z are the same")
else:
    print("w and z are not the same")
