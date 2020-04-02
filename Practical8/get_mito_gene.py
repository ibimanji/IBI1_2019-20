# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:01:19 2020

@author: yly
"""
import re
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as xfile:
    with open('mito_gene.fa','w')as yfile:
        all = xfile.read()
        pattern = re.compile(r'^>[^:]+:[^:]+:Mito:[^\n]+$\n(?:^[\w]+$\n)+^', re.M)
        list = pattern.findall(all)
        for ele in list:
            segments = ele.split(' ')
            name = segments[3][5:]
            sequence = segments[-1]
            sequence = ''.join(sequence.split('\n')[1:])
            a='>'+name+str(len(sequence))+'\n'+sequence+'\n'
            yfile.write(a)
            
            