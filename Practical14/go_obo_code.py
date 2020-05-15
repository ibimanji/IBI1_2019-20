# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:57:34 2020

@author: yly
"""
# import necessary libraries
import xml.dom.minidom
import pandas as pd
import os

print('please be patient with the loading time :)')

os.chdir(r"C:\Users\yly\desktop\IBI\IBI1_2019-20\practical14")#swich path
DOMTree=xml.dom.minidom.parse('go_obo.xml') #using DOM to parse go_obo.xml

collection=DOMTree.documentElement #root
terms=collection.getElementsByTagName('term')

defs=[]
is_a=[]
dic={}

for term in terms:
    definitions=term.getElementsByTagName('def')
    IDs=term.getElementsByTagName('id')[0]
    is_as=term.getElementsByTagName('is_a')#get 'is_a'
    for x in is_as:
        is_a.append(x.childNodes[0].data)
    dic[IDs.childNodes[0].data]=is_a[:]
    is_a.clear()
    for definition in definitions:
        defstr=definition.getElementsByTagName('defstr')[0]
        defs.append(defstr.childNodes[0].data)    
#count the number of 'autophagosome'
a=[]
for x in range(len(defs)):
    if 'autophagosome' in defs[x]:
        a.append(x)
#store the detailed information
ids=[]
names=[]
d=[]
for i in a:
    IDs=terms.item(i).getElementsByTagName('id')[0]
    ids.append(IDs.childNodes[0].data)
    NAMEs=terms.item(i).getElementsByTagName('name')[0]
    names.append(NAMEs.childNodes[0].data)
    d.append(defs[i])
    
#find the number of childnodes
childnode = []
for i in ids:
    m = []
    count = 0
    for j in dic:
        if i in dic[j]:
            count += 1#count a the general list
            m.append (j)
    n = m[:]
    inc = count
    while inc != 0 :#count a single list
        m = []
        inc = 0
        for k in n:
            for j in dic:
                if k in dic[j]:
                    count += 1#count the total elements
                    inc += 1
                    m.append (j)
        n = m[:]
    childnode.append (count)
        
#output the data into an excel file
data={'id':ids,'name':names,'definition':d,'childnodes':childnode}
dataframe=pd.DataFrame(data)
dataframe.to_excel(r'autophagosome.xlsx')

print('DONE!')
