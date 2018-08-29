
def circles_intersect(x1, y1, r1, x2, y2, r2):
    if r1 > r2 and r1 > abs(x1-x2) and r1 > abs(y1 - y2):
        return False
    if r2 > r1 and r2 > abs(x1-x2) and r2 > abs(y1 - y2):
        return False
    if abs(x1 - x2) > r1+r2:
        return False
    if abs(y1 - y2) > r1+r2:
        return False
    else:
        return True
a = circles_intersect(0, 0, 2, 0, 0.2, 1.91)
print(a)