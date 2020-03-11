nums = []
while(True):
    num = int(input())
    if(num == 9999):
        break
    nums.append(num)

nums.sort()

print(nums[0])