a=input()
n =int(input())
m=0
c=n
while n > 0:
    m=m*10 + n%10
    n//=10;
if m==c:
    print(c,"la so thuan nghich", end='')
else:
    print(c,"khong phai so thuan nghich", end='')