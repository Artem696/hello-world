# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:14:41 2020

@author: artni
"""

list1=[None,5,0.5,"art",[1,2,3],(True,1),{"ok":2,True:5}]
for elem in list1:
    print(type(elem))
list1.pop()

name=list("Horev Artem")
print(name)

name2=''.join(name)
print(name2)

for letter in enumerate(name2, 1):
    print(letter)

num=name.count("a")
print(num)