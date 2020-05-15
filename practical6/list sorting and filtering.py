# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:10:50 2020

@author: yly
"""
#input a list of 10 velues
g=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#sort to rank the element in the list from the smallest to the largest
g.sort()
#remove the the first,that is,the smallest one
del(g[0])
#remove the the last one,thatis,the largest one
del(g[-1])
#show the sorted gene list
print("sorted gene list is: ",g)

##draw a boxplot
import matplotlib.pyplot as plt
#set specific parameters
score=g
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False)
plt.title('list sorting and filtering') #add title
plt.show()
