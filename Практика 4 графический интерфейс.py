# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:55:14 2020

@author: artni
"""
import math
import collections

class Coder:
    word = ''
    word2=''
    dict2 = {}
    result= ""
    res_dec=""
    def coder(self):
        sum = 0.0        
        mass = [] 
        for i in range(0, 32):
            mass.append(0)
        dict1 = {
        'а':[mass[0],0,0.0,''],
        'б':[mass[1],0,0.0,''],
        'в':[mass[2],0,0.0,''],
        'г':[mass[3],0,0.0,''],
        'д':[mass[4],0,0.0,''],
        'е':[mass[5],0,0.0,''],
        'ж':[mass[6],0,0.0,''],
        'з':[mass[7],0,0.0,''],
        'и':[mass[8],0,0.0,''],
        'й':[mass[9],0,0.0,''],
        'к':[mass[10],0,0.0,''],
        'л':[mass[11],0,0.0,''],
        'м':[mass[12],0,0.0,''],
        'н':[mass[13],0,0.0,''],
        'о':[mass[14],0,0.0,''],
        'п':[mass[15],0,0.0,''],
        'р':[mass[16],0,0.0,''],
        'с':[mass[17],0,0.0,''],
        'т':[mass[18],0,0.0,''],
        'у':[mass[19],0,0.0,''],
        'ф':[mass[20],0,0.0,''],
        'х':[mass[21],0,0.0,''],
        'ц':[mass[22],0,0.0,''],
        'ч':[mass[23],0,0.0,''],
        'ш':[mass[24],0,0.0,''],
        'щ':[mass[25],0,0.0,''],
        'ъ':[mass[26],0,0.0,''],
        'ы':[mass[27],0,0.0,''],
        'ь':[mass[28],0,0.0,''],
        'э':[mass[29],0,0.0,''],
        'ю':[mass[30],0,0.0,''],
        'я':[mass[31],0,0.0,'']
        }
    
        def trans(a, l):
            num = ""
            for i in range(0,l):
                a = a * 2.0
                num += str(math.trunc(a))
                if a >= 1.0:
                    a -= 1.0
            return num
        for wordmin in self.word:
            dict1[wordmin][0] += 1

        for k in dict1.keys():
            if dict1[k][0] != 0.0:
                dict1[k][0] /= len(self.word)
                dict1[k][1] = math.ceil(math.log2(float(dict1[k][0]))*(-1))

        self.dict2.update(collections.OrderedDict(sorted(dict1.items(),key = lambda i:i[1][0],reverse=-1)))

        for k in self.dict2.keys():
            self.dict2[k][2] = sum
            sum += self.dict2[k][0]
            self.dict2[k][3] = trans(self.dict2[k][2],self.dict2[k][1])
        for w in self.word:
            #print(self.dict2[w][3])
            self.result+=self.dict2[w][3]
            self.word2 += self.dict2[w][3]
        print(self.result)
    
    def Decoder(self):
        string = ''
        dict3 = {}
        for k,i in self.dict2.items():
            dict3[i[3]] = k
        for i in self.word2:
            string += i
            try:
                dict3[string]
                self.res_dec+=dict3[string]
            except:
                pass
            else:
                print(dict3[string], end = '')
                string = ''
        print()       
                        

word = Coder()


import tkinter as tkn
from tkinter import filedialog as fd

def read_file():
    file_name = fd.askopenfilename(filetypes=(("texts", "*.txt"), ("All files", "*.*")))
    f = open(file_name, 'r')
    print(f.read())
    f.close()
def Coderr():
    try:  
        a = entry_a.get().lower()
        word.word=a
        word.coder()
        #l = (''.join(format(ord(x), 'b') for x in word.word))
        #print("Сжалось в {} раз".format(len(l)/len(word.word2)))
        #word.Decoder()
        label_result['text'] =str(word.result)
        print(word.result)
    except Exception:
        label_result['text'] = 'Ошибка'
def write_file():
    with open('text.txt', 'w') as f:
        a=entry_a.get().lower()
        f.write(str(a)) #str(word.result)
        f.close()
def write_results():
    with open('text.txt', 'w') as f:
        f.write(str(word.result))
        f.close()
def original_file():
    with open('text.txt', 'r') as f:
        for lines in f.readlines():
            label_orig_file["text"]=str(lines)
        f.close()
def coder_for_file():
    with open('text.txt', 'r') as f:
        for lines in f.readlines():
            b=str(lines)
        try:
            word.word=b
            word.coder()
            #l = (''.join(format(ord(x), 'b') for x in word.word))
            #word.result.append("Сжалось в {} раз".format(len(l)/len(word.word2)))
            #word.Decoder()
            label_result_file['text'] =str(word.result)
        except Exception:
            label_result_file['text'] = 'Ошибка'
        f.close()
def bin_cod():
    result_bin = []
    for i in range(len(word.result) // 8 + 1):
        res_cut = word.result[i*8:(i+1)*8]
        if len(res_cut) == 8:
            result_bin.append(int(res_cut,2))
    else:
        res_cut = res_cut + '0'*(8 - len(res_cut))
        result_bin.append(int(res_cut,2))

    result_bin = bytearray(result_bin)
    print(result_bin)
# преобразовать result в bytes
    f = open('text.txt', mode='wb')
    f.write(result_bin)
    f.close()
    
def decoder():
    f = open('text.txt', mode='rb')
    result_readed = f.read()
    print(result_readed)
    f.close()
    result_open = ''
    for item in result_readed:
        res_bin = bin(item)[2:]
        if len(res_bin)!=8:
            res_bin = '0'*(8 - len(res_bin)) + res_bin
            result_open += res_bin
        else:
            result_open+=res_bin
    print(result_open)
    word.Decoder()
decoder()  
    
root = tkn.Tk()
root.wm_title('Алгоритм Шеннона')
root.wm_resizable(width=True, height=False)


entry_a = tkn.Entry(root)
entry_a.grid(row = 0)

label_result = tkn.Label(root)
label_result.grid(row = 9)
label_result_file = tkn.Label(root)
label_result_file.grid(row = 10)
label_orig_file = tkn.Label(root)
label_orig_file.grid(row = 11)


button1 = tkn.Button(root, text='Coder', command=Coderr)#, width=25,height=5,bg='black',fg='red',font='arial 14')
button1.grid(row = 3)

button2 = tkn.Button(root, text='Open', command=read_file)
button2.grid(row = 1)

button3 = tkn.Button(root, text='Write', command=write_file)
button3.grid(row = 5)

button4 = tkn.Button(root, text='Open original file', command=original_file)
button4.grid(row = 2)

button5 = tkn.Button(root, text='Coder for file', command=coder_for_file)
button5.grid(row = 4)

button6 = tkn.Button(root, text='Write results', command=write_results)
button6.grid(row = 6)

button7 = tkn.Button(root, text='bin', command=bin_cod)
button7.grid(row = 7)

button8 = tkn.Button(root, text='decoder', command=decoder)
button8.grid(row = 8)
root.mainloop()