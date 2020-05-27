from collections import deque

n, x, y = map(int, input().split())

ans = [0] * (n+1)

g = [[i+1, i-1] for i in range(n+1)]
#g[0].clear() pypyにclearなし
g[1].pop(1)
g[n].pop(0)

g[x].append(y)
g[y].append(x)

for i in range(1,n+1):
    q = deque()
    time = 0
    visit = [False] * (n+1)
    q.append((i, time))

    while(len(q) > 0):
        item = q.popleft()

        if visit[item[0]] == False:
            visit[item[0]] = True
            ans[item[1]] += 1
            for k in g[item[0]]:
                q.append((k, item[1]+1))

for i in range(1,n):
    print(ans[i]//2)
