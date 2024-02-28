import re

def exe2(string):
    pattern = '^ab{2,3}$'

    if re.match(pattern, string):
        return "Yes!"
    else:
        return "No!"

n = str(input("string жаз: "))
print(exe2(n))