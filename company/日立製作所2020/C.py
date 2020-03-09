from collections import deque

n = int(input())
t = [list(map(int, input().split())) for i in range(n-1)]



d = warshall_floyd(d)


q = deque()

for i in range(n-1):
    for j in range(i,n):
        if d[i][j] == 3:
            q.append((i, j))

if len(q) == 0:
    print(-1)
    exit()


#print(q, sep='\n')

ans = [i+1 for i in range(n)]
chk = [False for i in range(n)]

while q:
    now = q.popleft()
    if (ans[now[0]] + ans[now[1]])%3 == 0 or (ans[now[0]]+ans[now[1]])%3 == 0:
        chk[now[0]] = True
        chk[now[1]] = True
        pass
    else:
        if not chk[now[0]]:
            for i in range(n):
                if not chk[i]:
                    ans[now[0]], ans[i] = ans[i], ans[now[0]]
                    if (ans[now[0]] + ans[i])%3 == 0 or (ans[now[0]]+ans[i])%3 == 0:
                        chk[now[0]] = True
                        chk[i] = True
                        pass
                    else:
                        ans[i], ans[now[0]] = ans[now[0]], ans[i]
        elif not chk[now[1]]:
            for i in range(n):
                if not chk[i]:
                    ans[now[1]], ans[i] = ans[i], ans[now[1]]
                    if (ans[now[1]] + ans[i])%3 == 0 or (ans[now[1]]+ans[i])%3 == 0:
                        chk[now[1]] = True
                        chk[i] = True
                        pass
                    else:
                        ans[i], ans[now[1]] = ans[now[1]], ans[i]
        else:
            print(-1)
            exit()
print(*ans, sep=" ")
