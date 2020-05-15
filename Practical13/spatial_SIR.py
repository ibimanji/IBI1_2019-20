# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:45:45 2020

@author: yly
"""
# import necessary libraries 
import numpy as np 
import matplotlib . pyplot as plt
#set up the model parameters
β=0.3
γ=0.05

# make array of all susceptible population 
population = np. zeros ( (100 , 100) )
'''
First we randomly select the x and y coordinates 
of where the outbreak is happening and store this in an array called outbreak. 
Then we use this to address the person with those exact coordinates in our population array 
and change their status from 0 (susceptible) to 1 (infected)
'''
#choose outbreak point
outbreak = np.random. choice (range(100) ,2) 
population[outbreak[0],outbreak[1]]=1
'''
use a kind of heat map
colour each of the 10000 points on our map by state (susceptible or infected)
susceptible individuals are shown in dark purple
infected individuals in blue-green
recovered individuals in yellow
'''
plt.figure(figsize=(6,4),dpi=150)
plt.imshow( population , cmap='viridis', interpolation='nearest')
for i in range (0,100):
    #ﬁnd the infected points
    infectedIndex = np.where(population==1)
    #address all its neighbours
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect the neighbours
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! 
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
    # refresh the infected data
    infectedIndex = np.where(population==1)
    #some of the infected people recover
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        population[x,y]=np.random.choice(range(2),1,p=[1-γ,γ])[0] + 1 
    #plot the outcome for each loop
    plt.figure(figsize=(6,4),dpi=150) 
    plt.imshow( population , cmap='viridis', interpolation='nearest')