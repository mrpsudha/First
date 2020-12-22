# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 09:59:27 2019

@author: Sudha
"""


def rainaverage(l):
   aver = {}
   aver_count={}
   average_final=[]
   # added for simplicity
   # commiting through pycharm
   # will see if changes get reflected
   # ADDED ONE MORE COMMENT
   #added comment in main branch
   for i in l:
       if i[0]in aver.keys():
           aver[i[0]]=aver[i[0]]+i[1]
           aver_count[i[0]]=aver_count[i[0]]+1
       else:     
           aver[i[0]]=i[1]
           aver_count[i[0]]=1
   for i in sorted(aver.keys()):
       average_final.append((i,float(aver[i])/aver_count[i]))
   return average_final

def flatten(l):
    flat_result=[]
    for i in l:
        if type(i)==type([]):
            flat_result.extend(flatten(i))
        else:
            flat_result.append(i)
    return flat_result

###Practice Assignment

def orangecap(l):
    aggregate_matches={}
    for i in l.keys():
        for j in l[i].keys():
            if j in aggregate_matches.keys():
                aggregate_matches[j]=aggregate_matches[j]+l[i][j]
            else:
                aggregate_matches[j]=l[i][j]
    high_score=0
    result=('abc',0)
    for i in aggregate_matches.keys():
        if aggregate_matches[i]>high_score:
            result=(i,aggregate_matches[i])
            high_score=aggregate_matches[i]
    return result

def addpoly(p1,p2):
    order_p1=p1[0][1]
    order_p2=p2[0][1]
    result_order=max(order_p1,order_p2)
    result_order=4
    result=[]
    coeff1=0
    coeff2=0
    for i in range(result_order,-1,-1):
        for j in p1:
            if j[1]==i:
                coeff1=j[0]
        for j in p2:
            if j[1]==i:
                coeff2=j[0]
        if coeff1+coeff2<>0:
            result.append((coeff1+coeff2,i))
        coeff1=0
        coeff2=0
    return result

def multpoly(p1,p2):
    result=[]
    result_1=[]
    coeff=0
    for i in p1:
        for j in p2:
            result.append((i[0]*j[0],i[1]+j[1]))
    result_order=result[0][1]
    for i in range(result_order,-1,-1):
        for j in result:
            if j[1]==i:
                coeff=coeff+j[0]
        if coeff<>0:
            result_1.append((coeff,i))
        coeff=0
    return result_1


multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
#end of story
