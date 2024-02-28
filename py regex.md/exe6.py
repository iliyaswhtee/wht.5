import re

def exe6(string):
    return re.sub('[ ,.]', ':', string)

n = str(input("write something: "))
print(exe6(n))