#1 Create a generator that generates the squares of numbers up to some number N.
n = int(input())
a = (i**2 for i in range(n+1))
for i in range(n+1):
    print(next(a))

#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
n = int(input())
a = (i for i in range(0,n+1,2))
for i in a:
    print(i)

#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
n = int(input())
def divide_3_4(n):
    for i in range(n):
        if i %3 ==0 and i %4 == 0:
            yield i

for i in divide_3_4(n):
    print(i)

#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a,b):
    for i in range(a,b+1):
        if i**0.5 == int(i**0.5):
            yield i

a = int(input());b = int(input())

for i in squares(a,b):
    print(i)

#5 Implement a generator that returns all numbers from (n) down to 0.
n = int(input())
a = (i for i in range(n,0-1,-1))
for i in a:
    print(i)