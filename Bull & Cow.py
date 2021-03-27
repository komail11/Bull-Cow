import random


def randint():
    num = random.randint(1000, 9999)
    return num


def game():
    randint()
    x = randint()
    print(x)
    while True:
        counta = 0
        countb = 0
        user = int(input("Choose a 4 Digit number:\n"))
        lisuser = [int(x) for x in str(user)]
        lisrand = [int(t) for t in str(x)]

        # Loop for Cow
        for i in range(0, len(lisuser)):
            if lisuser[i] == lisrand[i]:
                counta += 1

        # Loop for Bell
        for i in lisuser:
            if i in lisrand:
                countb += 1

        if user == x:
            print("You Won!")
            quit()

        else:
            print("Cow:",counta)
            print("Bull",countb)
            continue

game()