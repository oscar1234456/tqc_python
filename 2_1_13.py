a,b,c = eval(input())
d,e,f, = eval(input())

delta = (a*e) - (b*d)
dx = (c*e) - (b*f)
dy = (a*f) - (c*d)

if delta != 0:
    print("x is %.2f, y is %.2f" % ((dx/delta), (dy/delta)))
elif dx != 0 or dy != 0:
    print("無解")
else:
    print("無限多解")