a = int(input("Введите а:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if b < a:
    b, a = a, b
print(a,b,c)