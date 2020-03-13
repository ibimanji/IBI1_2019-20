# What does this piece of code do?
# Answer: This code aims to find a number between 1 and 100. This number cannot be divided by any integer between 2 and (the ceiling of n**0.5) plus 1.  

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    n = randint(1,100)
    u = ceil(n**(0.5))
    for i in range(2,u+1):
        if n%i == 0:
            p=False


     
print(n)


