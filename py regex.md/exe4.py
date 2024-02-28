import re

def exe4(string):
    pattern = '^[a-zA-Z]*$'

    if re.match(pattern, string):
        return "Yes!"
    else:
        "No!"

n = str(input("Сөз жазыңыз: "))
print(exe4(n))