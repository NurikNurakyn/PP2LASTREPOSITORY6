'''#1 A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams

def convert(grams):
    ounces = grams * 28.3495231
    return ounces
n = float(input("Enter grams to convert: "))
print(f"{n} grams =",round(convert(n),2),'ounces')


#2 Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def f_to_c(F):
    C = (5 / 9) * (F - 32)
    print(F,"Fahrenheit =",round(C,2), 'Celcium')
n1= float(input("Enter temperature in Fahrenheit: "))
f_to_c(n1) 


#3 Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads,numlegs):
    for i in range(numheads+1):
        j = numheads - i
        if (i*2 +j*4) ==numlegs:
            print('chicken =', i,'and rabbit =',j)
    else:
        return "No answer"
    
i1 = int(input('Heads count : '));j1 = int(input("Legs count : "))
solve(i1,j1)


#4 You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def prime(list):
    list1 = []
    for i in range(len(list)):
        a = True
        if list[i]<2:
            continue
        for j in range(2,int(list[i]**0.5) +1):
            if list[i]%j==0:
                a = False
                break
        if a:
            list1.append(list[i])
    return list1
list2 = list(map(int, input().split()))
print(prime(list2))


#6 Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def reverse1(l):
    l.reverse()
    print(l)
l1 = []
for i in input().split():
    l1.append(i)
reverse1(l1)


#7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    a = False
    for i in range(len(nums)-1):
        if (nums[i]==3 and (nums[i+1]==3)):
            a = True
    return a
    
ns = list(map(int,input().split()))
print(has_33(ns))


#8 Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    a = False
    for i in range(2,len(nums)):
        if nums[i]==7 and nums[i-1]==0 and nums[i-2]==0:
            a = True
    return a
ns1 = list(map(int,input().split()))
print(spy_game(ns1))


#9 Write a function that computes the volume of a sphere given its radius.
def vol_of_sphere(r):
    vol = (4/3)*(r**3)
    print(round(vol,3))
r = float(input())
vol_of_sphere(r)


#10 Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def unique_list(list):
    uniq = []
    for i in list:
        if i not in uniq:
            uniq.append(i)
    return uniq
unique = list(map(int,input().split()))
print(unique_list(unique))


#11 Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"

is_pal = input()
print(is_palindrome(is_pal))


#12 Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
def histogram(list):
    for i in range(len(list)):
        print(list[i]*'*')

histog = list(map(int,input().split()))
histogram(histog)

#13 Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
from random import randint
def guess_the_number():
    x = -1
    a = randint(1,20)
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    g = 0
    while x != a:
        g+=1
        x = int(input())
        if x>a:
            print("Your guess is too big.\nTake a guess.")
        elif x<a:
            print("Your guess is too low.\nTake a guess.")
        else:
            print(f'Good job, KBTU! You guessed my number in {g} guesses!')

guess_the_number()
'''