current = eval(input("Enter monthly saving amount:"))


for i in range(6):
    current *= (1+0.0123/12)

print("After the sixth month, the account value is %.2f" % current)