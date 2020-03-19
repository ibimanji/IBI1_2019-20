# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:44:24 2020

@author: yly
"""
#one method of counting
a='ATGCTTCAGAAAGGTCTTACG'
d={}
for b in a:
        d[b]=(d[b]+1)if (b in d) else(1)
print(d)
#another method of counting
str='ATGCTTCAGAAAGGTCTTACG'
str=','.join(str)
d={}
list=str.split(',')
for i in list:
    d[i]=list.count(i)
print (d)
#draw a pie chart
from matplotlib import pyplot as plt
labels='T','A','G','C'
sizes=[6,6,5,4]
explode=(0.05,0.05,0.05,0.05)
colors=['thistle','wheat','lavender','whitesmoke']
plt.pie(x=sizes,explode=explode,labels=labels,autopct='%2.1f%%',shadow=True,colors=colors)
plt.axis('equal')
plt.title('pie of the DNA nucleotides')
plt.show()

