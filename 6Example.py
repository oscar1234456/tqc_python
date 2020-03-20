import random
lotto = []
checkNum = []

for i in range(0, 50):
    checkNum.append(0)

count = 1
while count <= 6:
    randNum = random.randint(1, 49)
    if checkNum[randNum] == 0:
        lotto.append(randNum)
        count += 1
    checkNum[randNum] = 1

print('the lottery numbers are : \n', end = "")
for i in lotto:
    print(i, end=" ")
print()