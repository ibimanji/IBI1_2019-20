# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:44:24 2020

@author: yly
"""
#one method of counting
a=input('Please put in a DNA sequence:')
d={}
#accumulate the number of each nucleotide in the sequence
for b in a:
        d[b]=(d[b]+1)if (b in d) else(1)
print(d)

#another method of counting
str=input('Please put in a DNA sequence:')
str=','.join(str)
d={}
list=str.split(',')
for i in list:
    d[i]=list.count(i)
print (d)

from matplotlib import pyplot as plt
#draw a pie chart of the 4 DNA nucleotides
labels='T','A','G','C'#add labels
sizes=[6,6,5,4]#add values to sizes

'''
emphasize by specifying the fraction of the radius
with which to offset each wedge
'''
explode=(0.05,0.05,0.05,0.05)
colors=['thistle','wheat','lavender','whitesmoke']
plt.pie(x=sizes,explode=explode,labels=labels,autopct='%2.1f%%',shadow=True,colors=colors)
plt.axis('equal')#ensure that pie is drawn as a circle
plt.title('pie of the DNA nucleotides')
plt.show()

