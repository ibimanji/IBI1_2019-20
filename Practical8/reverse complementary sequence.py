# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:44:12 2020

@author: yly
"""
seq='ATGCGACTACGATCGAGGGCCAT'
a= {'A':'T','T':'A','C':'G','G':'C'}
b= [a[i]if i in a else i for i in seq]
d= b[::-1]
e= ''.join(d)
print('the reverse complementary sequence is:',e)

