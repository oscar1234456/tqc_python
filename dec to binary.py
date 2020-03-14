num = eval(input())

def decs (mul):
    if mul//2 == 0 : return str(mul%2)+"0"
    return str(mul%2) + decs(mul // 2)
def btod(mul):
    res = decs(mul)
    return res[len(res)::-1]

print(btod(num))


