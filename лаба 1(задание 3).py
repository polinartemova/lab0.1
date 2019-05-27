#3 задание
a=[int(i) for i in input("Введите список: ").split()]
#сумма элементов >10:
s=0
for i in a:
    if i>10:
        s=s+i

print("Сумма элементов >10=",s)
