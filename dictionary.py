def binhphuong(i):
    return i*i
square = {
    
}
a=input()
n =int(input())
for x in range(1,n+1):
    square.update({ x : binhphuong(x)});
print(square)