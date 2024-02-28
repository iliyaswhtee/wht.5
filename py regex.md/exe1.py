import re

def exe1(string):
    pattern = '^ab*' #Біздің шаблонымыз, яғни модель түрі
    
    if re.match(pattern, string):
        return "Yes!"
    else:
        return "No!"

n = str(input("string: "))
print(exe1(n))