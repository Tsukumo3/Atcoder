x, y = map(int, input().split())

a = []

for i in range(x+1):
    kame = 4*i
    turu = 2*(x-i)
    #print(kame, turu)
    a.append(kame+turu)

if y in a:
    print("Yes")
else:
    print("No")
