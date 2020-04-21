# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:12:19 2020

@author: yly
"""
import os
os.chdir(r"C:\Users\yly\desktop\IBI\IBI1_2019-20\Practical10")
##input files
#read the file SOD2_mouse.fa
m = open(r"C:\Users\yly\desktop\IBI\IBI1_2019-20\Practical10\SOD2_mouse.fa")
seqs = []
for line in m:
    if not line.startswith('>'):
        seqs.append(line.replace('\n',''))
m.close()
#merge list
sum_1=''
for seq in seqs:
    sum_1+=(str(seq))
sum_1=sum_1.upper()

#read the file RandomSeq
R = open(r"C:\Users\yly\desktop\IBI\IBI1_2019-20\Practical10\RandomSeq.fa")
seqs = []
for line in R:
    if not line.startswith('>'):
        seqs.append(line.replace('\n',''))
R.close()
#merge list
sum_2=''
for seq in seqs:
    sum_2+=(str(seq))
sum_2=sum_2.upper()

#read the file SOD2_human
h = open(r"C:\Users\yly\desktop\IBI\IBI1_2019-20\Practical10\SOD2_human.fa")
seqs = []
for line in h:
    if not line.startswith('>'):
        seqs.append(line.replace('\n',''))
h.close()
#merge list
sum_3=''
for seq in seqs:
    sum_3+=(str(seq))
sum_3=sum_3.upper()

##compare the hamming_distance between each amino acids
#the hamming_distance between mouse and random
hamming_distance_mR=0 #set initial distance as zero
for i in range(len(sum_1)): #compare each amino acid
    if sum_1[i] != sum_2[i]:
        hamming_distance_mR += 1 #add a score 1 if amino acids are different
print('the edit distance of mouse and random is:',hamming_distance_mR)
#the hamming_distance between mouse and human
hamming_distance_mh=0
for i in range(len(sum_1)):
    if sum_1[i] != sum_3[i]:
        hamming_distance_mh += 1
print('the edit distance of mouse and human is:',hamming_distance_mh)
#the hamming_distance between human and random
hamming_distance_Rh=0
for i in range(len(sum_2)):
    if sum_2[i] != sum_3[i]:
        hamming_distance_Rh += 1
print('the edit distance of random and human is:',hamming_distance_Rh)

##converts the txt format of BLOSUM62 to csv
import csv
csvFile = open("BLOSUM62.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []
f = open("BLOSUM62.txt",'r',encoding='GB2312')
l=f.readlines()
l1=['']
l1.extend(l[6].split())
writer.writerow(l1)
for line in l[7:]:
    csvRow = line.split()
    writer.writerow(csvRow)
f.close()
csvFile.close()
import pandas as pd
matrix=pd.read_csv("BLOSUM62.csv")

#create a function to check every line or every row
def check(x):
    k=0
    while True:
        if matrix.iloc[k,0] != x:
            k += 1
        if matrix.iloc[k,0] == x:
            break
    return k

##calculate the blosum score
#the blosum score of mouse and random
score_1=0
alignment_1=''
for i in range(len(sum_1)):
    xm = sum_1[i]
    xr = sum_2[i]   
    score_1 += matrix.loc[check(xr),xm]
    if xm == xr:
        alignment_1 += xm
    elif matrix.loc[check(xr),xm]>=0:
        alignment_1 += '+'
    else:
        alignment_1 += " "

#the blosum score of random and human
score_2=0
alignment_2=''
for i in range(len(sum_2)):
    x_r=sum_2[i]
    xh=sum_3[i]  
    score_2 += matrix.loc[check(xh),x_r]
    if x_r == xh:
        alignment_2 += x_r
    elif matrix.loc[check(xh),x_r]>=0:
        alignment_2 += '+'
    else:
        alignment_2 += " "
        
#the blosum score of human and mouse
score_3=0
alignment_3=''
for i in range(len(sum_3)):
    x_h=sum_3[i]
    x_m=sum_1[i]  
    score_3 += matrix.loc[check(x_m),x_h]
    if x_h == x_m:
        alignment_3 += x_h
    elif matrix.loc[check(x_m),x_h]>=0:
        alignment_3 += '+'
    else:
        alignment_3 += " "
        
#print out the result of each blosum score
print()
print('the score of mouse and random is:',score_1)
print(" mouse:{}".format(sum_1))
print("       {}".format(alignment_1))
print("random:{}".format(sum_2))
print()
print('the score of random and human is:',score_2)
print("random:{}".format(sum_2))
print("       {}".format(alignment_2))
print(" human:{}".format(sum_3))
print()
print('the score of human and mouse is:',score_3)
print(" human:{}".format(sum_3))
print("       {}".format(alignment_3))
print(" mouse:{}".format(sum_1))