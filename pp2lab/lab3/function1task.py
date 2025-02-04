
def convert(grams):
    ounces = grams * 28.3495231
    return ounces
n = float(input("Enter grams to convert: "))
print(f"{n} grams =",round(convert(n),2),'ounces')
 