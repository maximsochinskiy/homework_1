import math

def circles_intersect(x1, y1, r1, x2, y2, r2):
    if math.sqrt(math.pow((x1-x2), 2)+ math.pow((y1 - y2), 2)) <= r1 + r2 and math.sqrt(math.pow((x1-x2), 2)+ math.pow((y1 - y2), 2)) >= math.fabs(r1 - r2):
        return True
    else:
        return False


a = circles_intersect(0, 0, 1, 2, 0, 1)
print(a)
