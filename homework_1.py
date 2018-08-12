import math

#task No. 1
a = 10
b = 20
c = 30
d = a+b*(c/2)
print('Task 1: If a equals', a, 'and b equals', b, 'and c equals', c, 'then the equasion a+b*(c/2) will equial', d)

#task No. 2
a = 10
b = 20
c = 30
d = (a**2+b**2)%2
print('Task 2: If a equals', a, 'and b equals', b, 'then the equasion (a^2+b^2)%2 will equial', d)

#task No. 3
a = 10
b = 20
c = 30
d = (a+b)/12*c%4+b
print('Task 3: If a equals', a, 'and b equals', b, 'and c equals', c,
      'then the equasion (a + b)/12*c%4+b will equial', d)

#task No. 4
a = 10
b = 20
c = 30
d = (a-b*c)/(a+b)%c
print('Task 4: If a equals', a, 'and b equals', b, 'and c equals', c,
      'then the equasion (a-b*c)/(a+b)%c will equial', d)

#task No. 5
a = 10
b = 20
c = 30
d = abs(a-b)/(a+b)**3-math.cos(c)
print('Task 5: If a equals', a, 'and b equals', b, 'and c equals', c,
      'then the equasion |a-b|/(a+b)^3-cos(c) will equial', d)

#task No. 6
a = 10
b = 20
c = 30
d = (math.log(1+c)/-b)**4+abs(a)
print('Task 6: If a equals', a, 'and b equals', b, 'and c equals', c,
      'then the equasion |a-b|/(a+b)^3-cos(c) will equial', d)