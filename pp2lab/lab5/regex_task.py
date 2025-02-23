import re
with open("C:/Users/Админ/OneDrive/Рабочий стол/git/PP2LASTREPOSITORY6/pp2lab/lab5/row.txt","r", encoding="utf-8") as file:
    t = file.read()
#1
p1 = r'ab*'
m1 = re.findall(p1, t)
print(m1)

#2
p2 = r'ab{2,3}'
m2 = re.findall(p2, t)
print(m2)

#3
p3 = r'\b[a-z]+_[a-z]+\b'
m3 = re.findall(p3, t)
print(m3)

#4
p4= r'\b[A-Z][a-z]+\b'
m4 = re.findall(p4, t)
print(m4)

#5
p5 = r'\ba.*b\b'
m5 = re.findall(p5, t)
print(m5)

#6 
text = re.sub(r'[ ,.]',':',t)
print(t)

#7
text = "this_is_snake_case_string"
p7 = re.split(r'_', text)
text = p7[0] + ''.join(i.capitalize() for i in p7[1:])
print(text)  

#8
p8 = re.findall(r'[A-Z][a-z]*', t)
print(p8)

#9
p9 = re.sub(r'([A-Z])', r' \1', t)
print(p9)

#10
text = "ThisIsCamelCaseString"
p10 = re.sub(r'([A-Z])', r'_\1', text)
p10 = p10.lower().strip("_")
print(p10) 