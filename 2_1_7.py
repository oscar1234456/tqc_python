pay = eval(input())
cost = 0

if pay >= 38000:
    cost = pay * 7
elif pay >= 28000:
    cost = pay * 8
elif pay >= 18000:
    cost = pay * 9
elif pay >= 8000:
    cost = pay * 0.95

print(cost)



