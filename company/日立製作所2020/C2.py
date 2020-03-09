from collections import deque

n = int(input())
t = [list(map(int, input().split())) for i in range(n-1)]

def bfs(s, q):
    t = [None for i in range(n)]
    p = deque()
    t[s] = 0
    p.append(s)
    while p:
        now = p.popleft()
        next = d[now]#隣接リストを参照
        for di in next:
            if t[di] == None:
                t[di] = t[now] + 1
                if t[di] == 3:
                    q.append((s+1,di+1))
                else:
                    p.append(di)
    print(t)

#隣接リスト
d = [[] for i in range(n)]
for i in range(n-1):
    x,y = t[i]
    d[x-1].append(y-1)
    d[y-1].append(x-1)
q = deque()

for i in range(n):
    bfs(i, q)

#print(q, sep='\n')
if len(q) == 0:
    print(-1)
    exit()

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
        elif not chk[now[0]]:
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
