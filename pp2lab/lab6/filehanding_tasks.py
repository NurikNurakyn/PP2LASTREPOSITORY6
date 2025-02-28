import os
#1
print(os.getcwd())
path = input()
print("Directories:")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)

print("Files:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)
path = input("Specified path:")
for i in os.listdir(path):
    print(i)

#2
if os.path.exists(path):
    print("It exists")
    if os.path.isfile(path):
        print("This is file")
    elif os.path.isdir(path):
        print("This is directory")
    elif os.access("F_OK"):
        print("It exists")
    elif os.access("R_OK"):
        print("It is readability")
    elif os.access("W_OK"):
        print("It is writability")
    elif os.access("X_OK"):
        print("It is executability ")
else:
    print("Path doesnt exist")

#3
path = input()
if os.path.exists(path):
    print("It  exists")
    print(os.path.basename(path))
    print(os.path.dirname(path))

#4
f = open(r"C:\Users\Админ\OneDrive\Рабочий стол\git\PP2LASTREPOSITORY6\pp2lab\lab6\text.txt", 'r+')
print(len(f.readlines()),end="\n")

#5
list = ["SITE:IS",1,"Course"]
for i in list:
    f.write(str(i)+"\n" )
f.seek(0)
print(f.read())
f.close()

#6
A_Z = []
for i in range(65,91):
    A_Z.append(f"{chr(i)}.txt")
print(A_Z)

for i in A_Z:
    open(str(i),"x")

for i in A_Z:
    os.remove(i)

#7
f = open(r"C:\Users\Админ\OneDrive\Рабочий стол\git\PP2LASTREPOSITORY6\pp2lab\lab6\text.txt", 'r+')
copy = open(r"C:\Users\Админ\OneDrive\Рабочий стол\git\PP2LASTREPOSITORY6\pp2lab\lab4\sampledata.json", 'r+')
a = copy.read()
f.write(a)

#8
a = open("t.txt",'x')
a = open("t.txt",'r+')
path = input()
if os.path.exists(path):
    print("Object exists")
    if os.access(path,os.F_OK):
        print("File exists")
    elif os.access(path,os.R_OK):
        print("It is readability")
    elif os.access(path,os.W_OK):
        print("It is writability")
    elif os.access(path,os.X_OK):
        print("It is executability")
os.remove(path)



































