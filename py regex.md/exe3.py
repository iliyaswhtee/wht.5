import re

def exe3(string):
    pattern = '^[a-z]+(_[a-z]+)*$'

    if re.match(pattern, string):
        return "Yes!"
    else:
        return "No!"

n = str(input("сөз жазыңыз: "))
print(exe3(n))