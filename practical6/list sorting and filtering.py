# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:10:50 2020

@author: yly
"""
g=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
a=max(g)
b=min(g)
g.remove(a)
g.remove(b)
print(g)
import matplotlib.pyplot as plt
score=g
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False)
plt.title('list sorting and filtering')
plt.show()
