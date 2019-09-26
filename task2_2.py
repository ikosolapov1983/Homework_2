a = input("Введите значение:")
b = len(a)
if b == 2:
    a = int(a)
    a = a//10
    print(a)
else:
    print("Это не двузначное число")
