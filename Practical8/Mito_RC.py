# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:01:59 2020

@author: yly
"""
firename= input("please put in a firename:")
import re
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as xfile:
    with open(firename,'w')as yfile:
        all = xfile.read()
        pattern = re.compile(r'^>[^:]+:[^:]+:Mito:[^\n]+$\n(?:^[\w]+$\n)+^', re.M)
        list = pattern.findall(all)
        for ele in list:
            segments = ele.split(' ')
            name = segments[3][5:]
            sequence = segments[-1]
            sequence = ''.join(sequence.split('\n')[1:])
            d={'A':'T','T':'A','C':'G','G':'C'}
            c=[d[i]if i in d else i for i in sequence]
            s=''.join(c)
            a='>'+name+str(len(sequence))+'\n'+s[::-1]+'\n'
            yfile.write(a)
            