import re

def exe9(string):
    return re.sub('(?<!^)(?=[A-Z А-Я])', ' ', string)

n = str(input("Сөз жаз: "))
print(exe9(n)) 