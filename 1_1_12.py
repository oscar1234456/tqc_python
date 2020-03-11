import math
x = []
y = []

for i in range(3):
    tempX,tempY = eval(input())
    x.append(tempX)
    y.append(tempY)

dx1 = x[1]-x[0]
dy1 = y[1]-y[0]

dx2 = x[2]-x[1]
dy2 = y[2]-y[1]

dx3 = x[2]-x[0]
dy3 = y[2]-y[0]

side1 = ((dx1*dx1) + (dy1*dy1)) ** 0.5
side2 = ((dx2*dx2) + (dy2*dy2)) ** 0.5
side3 = ((dx3*dx3) + (dy3*dy3)) ** 0.5


s = (side1+side2+side3)/2

area = (s*(s-side1)*(s-side2)*(s-side3))**0.5

print("The area of the triangle = %.2f" % area)