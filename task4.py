a = int(input("Введите сторону а:"))
b = int(input("Введите сторону b:"))
c = int(input("Введите сторону c:"))
if a+b > c and a+c > b and b+c > a:
    print("Треугольник есть")
else:
    print("Не бывает такого треугольника")
