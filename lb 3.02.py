number = 7
running = True
while running:
    number2=(int(input("введите число")))
    if number == number2:
        print("вы угадали")
        running = False
    elif number2 > number:
        print("число меньше")
    else:
        print("число больше")
