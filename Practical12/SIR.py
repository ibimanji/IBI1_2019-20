# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:38:10 2020

@author: yly
"""
# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt
#deﬁne the basic variables of the model and create arrays
N = 10000
S = [9999]
I = [1]
R = [0]
β = 0.3
γ = 0.05
#The time course
'''
We will loop over 1000 time points. 
At each time point, we pick susceptible individuals at random to become infected. 
We pick infected individuals at random to become recovered. 
And we then keep track of the numbers of people in all three categories.
'''
T = [0]
for i in range (0,1000):
    a=np.random.choice(range(2),S[i],p=[1-β*(I[i]/N), β*(I[i]/N)])
    num_I= np.sum(a == 1)
    b=np.random.choice(range(2),I[i],p=[1-γ,γ])    
    num_R= np.sum(b == 1)
    S.append(S[i]-num_I)
    I.append(I[i]+num_I-num_R)
    R.append(R[i]+num_R) 
    T.append(i) 
#A note on probabilities
'''
The recovery probability for each infected individual is just γ
For a susceptible individual to be infected, 
consider not only the infection rate upon contact (β), 
but also the probability of making contact with an infected individual. 
'''
#plot the results
x_1 = T
x_2 = T
x_3 = T
y_1 = S
y_2 = I
y_3 = R
plt.figure(figsize=(6,4),dpi=150) #set width, height and sharpness
plt.plot(x_1,y_1,label='susceptible',color='blue',linestyle='-',linewidth=1.5)
plt.plot(x_2,y_2,label='infected',color='orange',linestyle='-',linewidth=1.5)
plt.plot(x_3,y_3,label='recovered',color='green',linestyle='-',linewidth=1.5)
plt.legend(loc='upper right')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.grid(alpha=0.2) #add grid and adjust transparency
plt.savefig('the SRI figure', type='png')
plt.show()










