# 1 lab.ry - файл
# lab.txt a b c d - текстовый файл
 # 2047(10) -
 # a % 2 == 0 - esli tak to ydovletvor yslovie
 # 2 ** 11(ctepen) > a
 # int - dla chisla vsegda, tok celie chisla = str(int[a

import re #bibleotek

slovar = {"0": "ноль", '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}

def Ermolaev(text):
    with open(text, "r") as file:
        ch = file.read().split()
    
    num = [int(a, 2) for a in ch if re.fullmatch(r'[01]*0[01]0',a)and int(a, 2)<=2047]#vce sovpadenia re.fullmatch
    
    if num:
        for numbers in num:
            print("".join(c for c in str(numbers) if c != "0"))
        
        print(" ".join(slovar[d] for d in str((min(num) + max(num)) // 2)))

Ermolaev("1.txt")
