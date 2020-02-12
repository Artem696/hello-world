# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:01:05 2020

@author: artni
"""
list=[0,1,2,3,4,5,6,7,8,9,10]
for num in list:
    print (num)
num=0
while 0<=num<=10:
    print (num)
    num+=1
Name="Artem Horev"
for let in Name:
    print(let)
list1=["Danil","Artem","Max"]
for name in list1:
    print(name)
dict={"Max":"15.12.2000","Hikita":"23.05.2000","Denis":"10.09.2000"}
for friend in dict:
    if dict[friend][3:5]=="06" or dict[friend][3:5]=="07" or dict[friend][3:5]=="08" or dict[friend][3:5]=="12" or dict[friend][3:5]=="01" or dict[friend][3:5]=="02":
        print(friend,dict[friend])
    