import random

while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print("%d + %d = " % (num1, num2))
    res = eval(input())
    if res != num1+num2 :
        print("Over!")
        break
    else:
        print("Correct!")

