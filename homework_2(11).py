import math
def degrees2radians(degree):
    rad = degree*(math.pi/180)
    return rad

result = degrees2radians(180)
print('Result: %.2f' %result)