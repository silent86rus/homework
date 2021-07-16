import random

print("Добро пожалоть в наше развлекательное заведение, как я могу к Вам обращаться?")

name = input("Меня зовут: ")
deposit = 10000
print("Суть нашей игры заключается в том, чтоб угадать случайно сгенерированое компьютером число от 2 до 12")
print("На Ваш депозит зачислено ", deposit, "рублей")
print("Компьютер генерирует число")


x = random.randint(2, 12)


number = int(input("назовите любое число от 2 до 12 "))


if number <= 12 and number >= 2:
    print("Ваше число: ", number)

else:
    print("Вы должны назвать число от 2 до 12")

if number == x:
    print("Ты выиграл 1000 рублей")
    deposit = deposit + 1000
    print("Твой баланс на депозите: ", deposit)
else:
    print("Ты проиграл 1000 рублей")
    deposit = deposit - 1000
    print("Твой баланс на депозите: ", deposit)

while deposit != 0:
    number = int(input("назовите любое число от 2 до 12 "))
    if number <= 12 and number >= 2:
        print("Ваше число: ", number)

    else:
        print("Вы должны назвать число от 2 до 12")

    if number == x:
        print("Ты выиграл 1000 рублей")
        deposit = deposit + 1000
        print("Твой баланс на депозите: ", deposit)
    else:
        print("Ты проиграл 1000 рублей")
        deposit = deposit - 1000
        print("Твой баланс на депозите: ", deposit)

print("Игра окончена. У Вас закончились деньги!")