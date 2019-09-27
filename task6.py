a = int(input("Введите а:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
count = 0
if a != b:
    count += 1
if b != c:
    count += 1
if c != a:
    count += 1
print("Количество совпадений: ", count)
