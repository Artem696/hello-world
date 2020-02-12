# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:18:08 2020

@author: artni
"""

enter=int(input("enter a number from -100 to 100: "))
if enter<-100:
    print("Low")
elif enter>100:
    print("High")
else:
    print("Yes")
print("enter<-50")
if enter<-50:
    print("yes")
else:
    print("no")
print("enter==-50")
if enter==-50:
    print("yes")
else:
    print("no")
print("-50<enter<0")
if -50<enter<0:
    print("yes")
else:
    print("no")
print("0<enter<50")
if 0<enter<50:
    print("yes")
else:
    print("no")
print("enter==50")
if enter==50:
    print("yes")
else:
    print("no")
print("enter>50")
if enter>50:
    print("yes")
else:
    print("no")