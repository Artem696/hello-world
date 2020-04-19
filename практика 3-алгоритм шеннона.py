import math
import collections

class Coder:
    word = ''
    word2=''
    dict2 = {}
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
        def Translate(a, l):
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
            self.dict2[k][3] = Translate(self.dict2[k][2],self.dict2[k][1])
        for w in self.word:
            print(self.dict2[w][3])
            self.word2 += self.dict2[w][3]
    def Decoder(self):
        string = ''
        dict3 = {}
        for k,i in self.dict2.items():
            dict3[i[3]] = k
        for i in self.word2:
            string += i
            try:
                dict3[string]
            except:
                pass
            else:
                print(dict3[string], end = '')
                string = ''
        

        
word = Coder()
word.word = input("Введите слово: ").lower()
word.coder()

print()
l = (''.join(format(ord(x), 'b') for x in word.word))
print("Сжалось в {} раз".format(len(l)/len(word.word2)))
word.Decoder()