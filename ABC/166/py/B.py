n , k = map(int, input().split())
d = []
a = []

for i in range(k):
    d.append(int(input()))
    a.append(list(map(int, input().split())))

l = [0]*n

for i in a:
    for j in i:
        l[j-1] += 1

ans = 0
for i in l:
    if i == 0:
        ans += 1
print(ans)
