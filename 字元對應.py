str = input()

count = 0
for i in range(len(str)):
    asc = ord(str[i])
    count+=asc
    print("ASCII code for '%s' is %d" % (str[i],asc))

print(count)