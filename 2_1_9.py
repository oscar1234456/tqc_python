x = eval(input())
y = eval(input())

dx = x - 5
dy = y - 6

dis = ((dx*dx) + (dy*dy))**0.5

if dis <= 15:
    print("Inside")
else:
    print("Outside")
