#ввод списка произвольной длины через пробел
a=[int(i) for i in input("Введите список: ").split()]
#вывод максимального числа из списка:
n=max(a)
print("Максимальный элемент=",n)
