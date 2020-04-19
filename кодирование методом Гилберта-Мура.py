# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 23:43:12 2020

@author: artni
"""
import math
word=input("Enter: ").lower()
dict2={}
pr=0
result=""
def Translate(q, l):
    num = ""
    for i in range(0,l):
        q = q * 2.0
        num += str(math.trunc(q))
        if q >= 1.0:
            q -= 1.0
    return num

    
for i in word:
    dict2[i]=i

for i in dict2:
    dict2[i]=0
for i in dict2:
    dict2[i]=[0,0,0,0,""]
for wordnum in word:
    dict2[wordnum][0]+=1

for j in dict2.keys():
    ver=dict2[j][0]/len(word)
    dict2[j][1]=ver
    

for i in dict2.keys():
    q=pr+dict2[i][1]/2
    dict2[i][2]=q
    pr+=dict2[i][1]
for j in dict2.keys():
    l=math.ceil(math.log2(float(dict2[j][1]))*(-1))+1
    dict2[j][3]=l

for h in dict2.keys():
    b=Translate(dict2[h][2],dict2[h][3])
    dict2[h][4]=b
for i in word:
    result+=dict2[i][4]

def decod():
    string = ''
    dict3 = {}
    for g,t in dict2.items():
        dict3[t[4]] = g
    print(dict3)
    for y in result:
        string += y
        try:
            dict3[string]
        except:
            pass
        else:
            print(dict3[string], end = '')
            string = ''
decod()     
print(" ")      
L_avg=0.0
redund=0.0
for h in word:
    L_avg+=dict2[h][1]*dict2[h][3]
    redund+=-(dict2[h][1]*math.log2(dict2[h][1]))    
        
print("Неравенство: ",L_avg,"<",redund+2)
if L_avg<redund+2:
    print("Неравенство выполняется")
else:
    print("Неравенство не выполняется")