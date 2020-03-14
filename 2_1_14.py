num = input()

renum = num[len(num)::-1]

if renum == num:
    print(num+" is a palindrome number.")
else:
    print(num+" is not a palindrome number.")


