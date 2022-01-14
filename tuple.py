import re
a=input()
print(a)
l=re.findall(r'\d', a)
t=tuple(l)
n=len(l)
m=len(a)
b=a[0: m-n]
c=tuple(b)
print(c)
print (l)
print (t)