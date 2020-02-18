# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:31:53 2020

@author: artni
"""
import winsound
import time
a=input("Enter a word: ")
a=a.lower()
list1= list(a)
list2=[]
morse = {'а': '.-',
         'б': '-...',
         'в': '.--',
         'г': '--.',
         'д': '-..',
         'е': '.',
         'ж': '...-',
         'з': '--..',
         'и': '..',
         'й': '.---',
         'к': '-.-',
         'л': '.-..',
         'м': '--',
         'н': '-.',
         'о': '---',
         'п': '.--.',
         'р': '.-.',
         'с': '...',
         'т': '-',
         'у': '..-',
         'ф': '..-.',
         'х': '....',
         'ц': '-.-.',
         'ч': '---.',
         'ш': '----',
         'щ': '--.-',
         'ъ': '.--.-.',
         'ы': '-.--',
         'ь': '-..-',
         'э': '..-..',
         'ю': '..--',
         'я': '.-.-'}
for i in morse:
    for ind in list1:
        if i==ind:
            list2.append(morse[i])

frequency = 1000
for set in list2:
    for symbol in set:
        if symbol == '.':
            winsound.Beep(frequency, 200)
        elif symbol == '-':
            winsound.Beep(frequency, 800)
    print()
    time.sleep(0.9)
