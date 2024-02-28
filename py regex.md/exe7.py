import re

def exe7(string):
    return ''.join(x.capitalize() or '_' for x in string.split('_'))

snake = str(input("стринг жаз: "))
CamelStr = exe7(snake)

print(CamelStr)