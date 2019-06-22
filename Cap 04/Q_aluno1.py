import math

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

#d = ((x2-x1)^2 + (y2-y1)^2) * 1/2

xt = x2-x1
yt = y2-y1

xt = math.pow(xt,2)
yt = math.pow(yt,2)

d = math.sqrt(xt+yt)
print(d)
