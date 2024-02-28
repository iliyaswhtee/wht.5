import re

def exe8 (string):

    return re.split('(?=[A-Z])', string)

n = str(input("Сөз жаз:"))
print(exe8(n))