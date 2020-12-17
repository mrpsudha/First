# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:20:02 2019

@author: Sudha
"""

books={}
borrowers={}
checkouts=[]
lines=[]
def fun1():  
    
    global lines
    a=input()
    lines.append(a)
    while a!="EndOfInput":
        a = input()
        lines.append(a)
    #print lines
    global checkouts
    global books
    global borrowers
    count=0
    for i in range(1,len(lines)):
        if lines[i]=='Borrowers':
            count=1
        if lines[i]=='Checkouts':
            count=2
        if count==0:
            books[lines[i].split('~')[0]]=lines[i].split('~')[1]
        if count==1 and lines[i]!="Borrowers":
            borrowers[lines[i].split('~')[0]]=lines[i].split('~')[1]
        if count==2 and not(lines[i]=="EndOfInput" or lines[i]=="Checkouts"):
            checkouts.append(lines[i].split('~'))

    for i in range(len(checkouts)):
        checkouts[i][0]=borrowers[checkouts[i][0]]
    sorting(checkouts)
    #return checkouts
    
def sorting(l):
        for i in range(len(l)):
            for j in range(len(l)):
                idate=l[i][2].split('-')
                jdate=l[j][2].split('-')
                if (idate[0]*10000+idate[1]*100+idate[2])==(jdate[0]*10000+jdate[1]*100+jdate[2]):
                    if l[i][0]<l[j][0]:
                        l[i],l[j]=l[j],l[i]
                elif (idate[0]*10000+idate[1]*100+idate[2])<(jdate[0]*10000+jdate[1]*100+jdate[2]):
                    l[i],l[j]=l[j],l[i]
fun1()    
fin_lis=[]
lis=[]
for i in range(len(checkouts)):
    #print('{0}~{1}~{2}~{3}'.format(checkouts[i][2],checkouts[i][0],checkouts[i][1],books[checkouts[i][1]]))
    
    lis=[checkouts[i][2],checkouts[i][0],checkouts[i][1],books[checkouts[i][1]]]
    fin_lis.append('~'.join(lis))
fin_lis.sort()
for i in range(len(fin_lis)):
    print fin_lis[i]
#print(str(checkouts[i][2])+'~'+str(borrowers[checkouts[i][0]])+'~'+str(checkouts[i][1])+'~'+str(books[checkouts[i][1]]))
#print('{}'~'+borrowers[checkouts[i][0]]+'~'+checkouts[i][1]+'~'+books[checkouts[i][1]]'.format(checkouts[i][2]))
#print('~'.join(lis))
#print(checkouts[i][2],checkouts[i][0],checkouts[i][1],books[checkouts[i][1]],sep="~")