"""
#1 
import functools
list = [1,2,3,4,5]
multipy = functools.reduce(lambda x,y: x*y,list)
print(multipy)

#2
string = input()
upper = []
lower = []
digit = []
for c in string:
    if c.isupper():
        upper.append(c)
    elif c.islower():
        lower.append(c)
    elif c.isdigit():
        digit.append(c)
print("Upper case count:",len(upper))
print("Lower case count:",len(lower))
print("Digit count:",len(digit))

#3 
def palindrome(s):
    s1 = s.lower()
    if s1[::-1]== s1:
        print("This string is palidrome")
    else:
        print("This string is not palindrome")
s = input()
palindrome(s)

#4
import time 
import math
n = int(input())
t = float(input())/1000
print(f"Square root of {n} after {t*1000} miliseconds is",end=" ")
time.sleep(t)
print(math.sqrt(n))
"""
#5
tuple = ("1",4,True,1,"Yes")
tuple1 = ("",0,False,"-","No")
tuple2 = ()
print(all(tuple))
print(all(tuple1))
print(all(tuple2))