import re

def exe5(string):
    pattern = '^a.*b$'

    if re.match(pattern, string):
        return "Yes!"
    else:
        return "No!"

n = str(input("write something: "))
print(exe5(n))