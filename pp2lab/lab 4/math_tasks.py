import math
'''
#1 Write a Python program to convert degree to radian.
degree = int(input('Input degree: '))
radian = math.radians(degree)
print('Output radian:',round(radian,6))

#2 Write a Python program to calculate the area of a trapezoid.
h = int(input("Height: "))
a = int(input('Base, first value: '))
b = int(input('Base, second value: '))
area = h*((a+b)/2)
print('Expected Output:',round(area,2))
'''
#3 Write a Python program to calculate the area of regular polygon.
n = int(input('Input number of sides:'))
s = int(input('Input the length of a side:'))
area = round((n*(s**2)/(4*math.tan((math.pi)/n))),2)


print('The area of the polygon is:',area)

#4 Write a Python program to calculate the area of a parallelogram.
a = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
area = a*h
print("Expected Output:",area)