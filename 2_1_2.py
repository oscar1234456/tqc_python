num = eval(input())
isMod3 = (num % 3) == 0
isMod5 = (num % 5) == 0
msg = "is a multiple of"
if isMod3 and isMod5:
    print(num, msg, "3 and 5")
elif isMod3:
    print(num, msg, 3)
elif isMod5:
    print(num, msg, 5)
else:
    print(num, "is not a multiple of", "3 or 5")