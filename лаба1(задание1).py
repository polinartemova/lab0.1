#задание 1
a=float(input("Введите а"))
b=float(input("Введите b"))
c=float (input("Введите c"))
k=float (input("Введите k"))
if (b==0)or(a==0):
    print("Ошибка! Делить на ноль низя")
else:
    y=(a+b+c*(k-a/b**3))
    if(y==0):
        print("Ошибка!Делить на ноль низя")
    else:
        x=abs((a**2/b**2+c**2*a**2)/y+c+(k/b-k/a)*c)
        print("Решение примера:",x)
