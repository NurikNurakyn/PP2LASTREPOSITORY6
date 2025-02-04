'''#1
def convert(grams):
    ounces = grams * 28.3495231
    return ounces
n = float(input("Enter grams to convert: "))
print(f"{n} grams =",round(convert(n),2),'ounces')

#2
def f_to_c(F):
    C = (5 / 9) * (F - 32)
    print(F,"Fahrenheit =",round(C,2), 'Celcium')
n1= float(input("Enter temperature in Fahrenheit: "))
f_to_c(n1) 

#3
def solve(numheads,numlegs):
    for i in range(numheads+1):
        j = numheads - i
        if (i*2 +j*4) ==numlegs:
            print('chicken =', i,'and rabbit =',j)
    else:
        return "No answer"
    
i1 = int(input('Heads count : '));j1 = int(input("Legs count : "))
solve(i1,j1)

#4
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
print(prime(list2))'''