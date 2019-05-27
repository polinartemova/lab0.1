import random
my_number=random.randint(0,50)
user_number=int(input("Введите число"))
if user_number<my_number:
    print("Ура! Вы ввели число меньше заданного.")
    print("Заданное число:",my_number)
else:
    while True:
        user_number=int(input("Ваше число больше заданного числа или равно ему.Введите число снова"))#Ввод значения и конвертирование в целое число
        if(user_number<my_number):
            print("Ура! Вы ввели число меньше заданного.")
            print("Заданное число:",my_number)
            break                   
