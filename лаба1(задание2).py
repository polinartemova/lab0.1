
#ввод списка произвольной длины через пробел
r=[int(i) for i in input("Введите список: ").split()]
#находим четные числа:
a=list(filter(lambda x:not int(x)%2,r))
if a:
    print("Все четные числа из списка:")
    for i in a: print(i)
else:
    print("Нет четных чисел")
