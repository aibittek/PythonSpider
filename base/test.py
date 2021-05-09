import re

var = 'aababaaabab'
print(re.findall(r'a.*b', var))