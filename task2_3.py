x = input("Введите значение:")
line = len(x)
if line == 3:
    a, b, c = int(x[0]), int(x[1]), int(x[2])
    x = a+b+c
    print(x)
else:
    print("Это не трехзначное число")
