# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:58:48 2020

@author: yly
"""
#using‘ ’to connect
n=int(input("please input a positive integer:"))
print(n,end=' ')
while n!=1:
    if n%2 ==0:
        n=int(n/2)
        print(n,end=' ')
    else:
        n=int(n*3+1)
        print(n,end=' ')

#using‘-’to connect
n=int(input("please input a positive integer:"))
l=[str(n)]
while n!=1:
    if n%2 ==0:
        n=int(n/2)
        l.append(str(n))
    else:
        n=int(n*3+1)
        l.append(str(n))
print('-'.join(l))
        
