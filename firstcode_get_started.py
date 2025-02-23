n = int(input())
m = int(input())

s = []
for i in range(n):
    a = []
    for j in range(m):
        b = int(input())
        a.append(b)
    s.append(a)

for i in range(n):
    for j in range(m):
        print(s[n][m],end=' ')
    print()