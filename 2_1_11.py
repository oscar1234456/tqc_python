while True:
    try:
        x, y = eval(input())
        break
    except:
        print("Please enter the number with \",\"!")


if -4 <= x <= 4 and -3 <= y <= 3:
    print("In")
else:
    print("Out")
