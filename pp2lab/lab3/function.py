def my_function():
  print("Hello from a function")
my_function()

#second part
def my_function1(fname):
  print(fname + " Refsnes")
my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

#third part
def my_function2(country = "Norway"):
  print("I am from " + country)
my_function2("Sweden")
my_function2("India")
my_function2()
my_function2("Brazil")

#fourth part
def my_function3(x):
  return 5 * x
print(my_function3(3))
print(my_function3(5))
print(my_function3(9))

#fifth part
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
