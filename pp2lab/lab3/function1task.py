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
'''

#7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    a = False
    for i in range(len(nums)-1):
        if (nums[i]==3 and (nums[i+1]==3)):
            a = True
    return a

ns = list(map(int,input().split()))
print(has_33(ns))