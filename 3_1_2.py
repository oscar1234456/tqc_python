a = eval(input())
b = eval(input())
count = 0

for i in range(a, b+1):
    if i % 2 == 0 :
        count += i

print(count)