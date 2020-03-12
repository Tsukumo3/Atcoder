n, m ,c  = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in a:
    s = 0
    for j in range(m):
        s += i[j]*b[j]
    s += c
    if s > 0:
        ans += 1
print(ans)
