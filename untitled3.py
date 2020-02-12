# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:21:56 2020

@author: artni
"""

def hel():
    print("Hello,world")
hel()

def fio(a):
    print (a)
fio("Artem")

def equat(a,b,c):
    D=b**2-4*a*c
    print (D)
equat(2,4,6)

def name():
    name=input("Enter your name: ")
    year=int(input("Enter your year: "))
    print (name)
    print (year)
name()

def fun(a):
    if a>33 and a<1:
        print("Error")
    else:
        a=a+1039
        print(chr(a))
fun(int(input("Enter a number(1-33): ")))