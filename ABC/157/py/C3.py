N, M = map(int, input().split())
s = []
c = []

for i in range(M):
    a, b = map(int, input().split())
    s.append(a)
    c.append(b)

ans = [None]*N

for i in range(M):

    if s[i] == 1 and c[i] == 0 and N != 1:
        print(-1)
        exit()
    if ans[s[i]-1] == None:
        ans[s[i]-1] = c[i]
    elif ans[s[i]-1] == c[i]:
        continue
    else:
        print(-1)
        exit()

if N == 1:
    if ans[0] == None:
        ans[0] = 0
else:
    if ans[0] == None:
        ans[0] = 1
    for i in range(1, N):
        if ans[i] == None:
            ans[i] = 0

print(*ans, sep="")
