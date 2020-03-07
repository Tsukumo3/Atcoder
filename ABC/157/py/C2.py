N, M = map(int, input().split())
s = []
c = []

for i in range(M):
    a, b = map(int, input().split())
    s.append(a)
    c.append(b)

ans = 0
for i in range(10*N):
    for j in range(M):
        target = str(i)

print(ans)
