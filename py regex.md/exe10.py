import re

def exe10(string):
    return re.sub('(?<!^)(?=[A-Z])', '_', string).lower()

camel = str(input("Напиши камель слово: "))
snake = exe10(camel)

print(snake)