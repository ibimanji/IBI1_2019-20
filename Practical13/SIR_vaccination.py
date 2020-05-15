# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:31:27 2020

@author: yly
"""
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#deﬁne the basic variables of the model and create arrays
N=10000
R=[0]
β=0.3
γ=0.05

for p in range (0,11):
 num_S=int(N*(10-p)/10)
 S=[num_S]
 T=[0]
 t=0
 I=[1]
 '''
 random.choice function with a probability
 count the number of people infected and recoverd
 Before moving on to the next time step
 record the output of each time step 
 '''
 for t in range (0,1000):
    a=np.random.choice(range(2),S[t],p=[1-β*(I[t]/N), β*(I[t]/N)])
    num_I= np.sum(a == 1)
    b=np.random.choice(range(2),I[t],p=[1-γ,γ])    
    num_R= np.sum(b == 1)
    S.append(S[t]-num_I)
    I.append(I[t]+num_I-num_R)
    R.append(R[t]+num_R) 
    T.append(t) 
 '''
 extend the model to include an additional group of vaccinated people(10% of the population)
 plots the dataset data using colour number 30 (a sort of blue) from the viridis colour map
 '''
 plt.plot(T,I,label=str(p*10)+'%',color=cm.viridis(p*30))
 plt.legend(loc='upper right')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.grid(alpha=0.2) #add grid and adjust transparency
plt.figure(figsize=(6,4),dpi =150) #set width, height and sharpness
plt.savefig('the SRI_vaccination figure', type='png')
plt.show()

