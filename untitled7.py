# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:04:30 2020

@author: artni
"""

def fun(a,b):
    if a==0:
        print("Error")
    elif b==0:
        print("Eroor")
    else:
        c=a/b
        print(c)
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
fun(a,b)
    