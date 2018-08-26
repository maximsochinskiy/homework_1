import math
def cone_square_and_volume(radius, height):
     square = math.pi * radius * math.sqrt(radius**2 + height**2)
     volume = (height / 3)* math.pi * radius**2
     return square, volume

result_square, result_volume = cone_square_and_volume(5, 4)

print('Results, are: %.2f, %.2f' % (result_square, result_volume))