import re
a=input()
print(a)
l=re.findall(r'\d', a)
t=tuple(l)
print (l)
print (t)