res = []
with open("read.txt", "r") as file:
    nums = file.readline()
    while nums != "":
        num = nums.split(" ")
        for i in range(0, len(num)):
            num[i] = num[i].replace("\n", "")
        res += num
        nums = file.readline()

count = 0
for i in range(len(res)):
    count += int(res[i])

print(count)
