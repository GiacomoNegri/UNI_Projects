# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:35:16 2023

@author: negri
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 23:05:06 2023

@author: giacomonegri
"""

import csv
import os
import string

os.chdir(r'C:\Users\negri\OneDrive\Documents\SCUOLA\UNI\MINOR C&DS\IntroduzioneProgrammazione\Progetto')

file = open('IMDBDataset_clean.csv',encoding="utf8")
csv_reader = csv.reader(file, delimiter=',')

#TASK 1
def opener(file):
    dic={}
    with open(file, 'r') as f:
        line=f.readlines()
        justwords=[word.strip() for word in line]
        return justwords

def converter(lit:list, dic:dict):
    if lit==[]:
        return dic['']=''
        if lit[0] in dic:
            dic[lit[0]]+=1
        else:
            dic[lit[0]]=1
        return converter(lit[1:],dic)

negdic={}
negwords=converter(opener('negative-words.txt'),negdic)
posdic={}
poswords=converter(opener('positive-words.txt'),posdic)

    

reviews=[]
valuations=[]
for row in csv_reader:
    reviews.append(row[0])
    valuations.append(row[1])

def list_to_dict_value0or(lit,booly):
    dic={}
    for thing in lit:
        if thing in dic:
            dic[thing]+=1
        elif booly==True:
            dic[thing]=0
        else:
            dic[thing]=1
    return dic

def opening_strip(file):
    with open(file, 'r') as f:
        words = f.readlines()
        justwords = [word.strip() for word in words]
        freq=list_to_dict_value0or(justwords,True)
        return justwords,freq
    
negwords,freq_negwords=opening_strip('negative-words.txt')
poswords,freq_poswords=opening_strip('positive-words.txt')


stripped_reviews=[]
for review in reviews:
    stripped_reviews.append(review.split())
    
def stran(totest,checkpos,checkneg,dic_poswords,dic_negwords):
    found=False
    dif=0
    adj_totest=totest.lower().translate(str.maketrans("","",string.punctuation))#because he differentiate between found_negative, found_positive and not_found    
    if adj_totest in checkpos:
        found=True
        dif=1
    if found==False and adj_totest in checkneg:
        dif=-1
    if dif>0:
        dic_poswords[adj_totest]+=1
    if dif<0:
        dic_negwords[adj_totest]+=1
    return dif


def counter(reviewtotest,checkpos,checkneg,dic_poswords,dic_negwords):
    m=0
    for word in reviewtotest:
        m+=stran(word,checkpos,checkneg,dic_poswords,dic_negwords)
    return m
    
scores=[]

for i in range(1,len(stripped_reviews)):
    result=counter(stripped_reviews[i], poswords, negwords,freq_poswords,freq_negwords)
    scores.append(result)


meanscores=sum(scores)/len(scores)
print("The mean score is: ", meanscores)
import numpy as np
stdscores=np.std(scores)
print("The standard deviation is:", stdscores)

#TASK 2
frequency = list_to_dict_value0or(scores, False)

def abs_to_rel(leng,dic):
    i=0
    dic_keys=list(dic.keys())
    for value in dic.values():
        dic[dic_keys[i]]=(value/leng)*100
        i+=1

abs_to_rel(len(scores), frequency)

def sortator(dic,booly):
    if booly==True:
        sorted_freq=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    else:
        sorted_freq=sorted(dic.items(),key=lambda x:x[0],reverse=False)
    return sorted_freq

def estrapolator(dic,booly):
    lit=[]
    if booly==True:
        lit=sortator(dic,True)[:20]
    else:
        lit=sortator(dic,False)
    lit_val=[]
    lit_words=[]
    for i in range(0,len(lit)):
        lit_words.append(lit[i][0])
        lit_val.append(lit[i][1])
    return lit_words,lit_val

sorted_keys, sorted_values=estrapolator(frequency,False)

def histogram(xlabel,ylabel,title,xaxis,yaxis,booly):
    import matplotlib.pyplot as plt
    
    fix,ax=plt.subplots()
    plt.bar(xaxis,yaxis)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid()
    if booly==True:
        ax.set_xticklabels(xaxis, rotation=90)
    else:
        pass
    plt.savefig(title+'.pdf')

histogram("Values of scores","Relative frequency","Relative Frequency of scores",sorted_keys,sorted_values,False)

#TASK 3
j=0
correctscores=0
relevantscores=len(scores)
for score in scores:
    j+=1
    if (score>1 and valuations[j]=='positive')or(score<-1 and valuations[j]=='negative'):
        correctscores+=1
    elif (score<=1 and score>=0):
        relevantscores-=1
    else:
        pass

accuracy=correctscores/relevantscores
print("The accuracy is (%): ",round(accuracy,4)*100,"\nNot accurate evaluation are (%): ", (1-round(accuracy,4))*100)

#TASK 4
sort_maxposwor,sort_maxposval=estrapolator(freq_poswords,True)
sort_maxnegwor,sort_maxnegval=estrapolator(freq_negwords,True)

histogram("Words","Frequency individual word","Frequency of positive words",sort_maxposwor,sort_maxposval,True)
histogram("Words","Frequency individual word","Frequency of negative words",sort_maxnegwor,sort_maxnegval,True)
