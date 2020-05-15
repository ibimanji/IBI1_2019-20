# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:58:48 2020

@author: yly
"""
##one way:using‘ ’to connect
#randomly input a positive interger
n=int(input("please input a positive integer:"))
print(n,end=' ')#using‘ ’to connect
while n!=1:
    if n%2 ==0: #if n is even
        n=int(n/2)#according to collatz sequence
        print(n,end=' ')#using‘ ’to connect
    else: #if n is odd
        n=int(n*3+1)#according to collatz sequence
        print(n,end=' ')#using‘ ’to connect

##another way:using‘-’to connect(looks better)
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
        
