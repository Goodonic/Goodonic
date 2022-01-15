import random
hp = 3
print('Попыток:', hp)
number = random.randint(1, 10)
for i in range(3):
    print("Введите число от 1 до 10")
    a = int(input())
    if a == number:
        print("ПОБЕДА!")
        break
    elif a != number:
        hp -= 1
        if a < number:
            print("Слишком мало")
        elif a > number:
            print("Слишком много")
        print("Попыток:", hp)
print('Правильный ответ:', number)
print("Нажмите 0 чтобы выйти")
exit = int(input())