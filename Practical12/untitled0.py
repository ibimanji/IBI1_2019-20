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

Id=[]#A list to store id
Name=[]#A list to store name
definition=[]#A list to store 'defstr'
childnodes=[]#A list to store number of nodes

def childnode(n1):
    global terms
    childnodes=0#Count the childnodes
    #get 'is_a'
    for term in terms:
        is_a=term.getElementsByTagName('is_a')
        for parent in is_a:
            #if n1 is parent
            if parent.childNodes[0].data==n1:
                childnodes+=1
                #count childnodes of the childnode
                n2=term.getElementsByTagName('id')[0].childNodes[0].data
                childnodes+=childnode(n2)
    return childnodes

#get all contents in <defstr>
for term in terms:
    defs=term.getElementsByTagName('def')[0]
    defstr=defs.getElementsByTagName('defstr')[0].childNodes[0].data
    #if 'autophagosome' is found
    if defstr.find('autophagosome')>-1 or defstr.find('Autophagosome')>-1:
        #get id, name, definition and add them to the lists 
        n1=term.getElementsByTagName('id')[0].childNodes[0].data
        Id.append(n1)
        Name.append(term.getElementsByTagName('name')[0].childNodes[0].data)
        definition.append(defstr)
        #get the number of childnodes and add to the list
        childnodes.append(childnode(n1))
        
#output the data into an excel file
file={'id':Id,'Name':Name,'definition':definition,'childnodes':childnodes}
dataframe=pd.DataFrame(file)
dataframe.to_excel(r'C:\Users\yly\desktop\IBI1\IBI1_2019-20\Practical14\autophagosome.xlsx')

print('DONE!')