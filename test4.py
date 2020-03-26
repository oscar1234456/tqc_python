nums = ()
nums2 = ()
while True:
    num = eval(input("1:"))
    if num == -9999:
        break;
    nums += (num,)


while True:
    num = eval(input("2:"))
    if num == -9999:
        break;
    nums2 += (num,)

nums = (nums+nums2)
print("Combined tuple before sorting :",nums)

list_num = list(nums)

list_num.sort()
print(list_num)