'''
#1 Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class String:
    def __init__(self):
        self.text = ''
    def getString(self):
        self.text=input()
    def printString(self):
        print(self.text)

s = String()
s.getString()
s.printString()

#2,3 Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Squera(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length**2
    
class Rectangle(Shape):
    def __init__(self,length,width):

        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    
#Shape
shape = Shape()
print(shape.area())

#Square
x = int(input('Enter the length of Square: '))
square = Squera(x)
print("Area of square:",square.area())

#Rectangle
a = int(input('Enter the length of Rectangle: '))
b = int(input('Enter the width of Rectangle: '))
rectangle = Rectangle(a,b)
print("Area of rectangle:",rectangle.area())
'''

#6 
list1 = list(map(int,input().split()))

prime = lambda x : all(x%i != 0 for i in range(2,round(x**0.5)+1)) if x > 1  else False
prime_list = list(filter(prime,list1))

print(prime_list)