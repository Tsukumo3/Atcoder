from collections import deque

h,w = map(int, input().split())
l = [list(input()) for _ in range(h)]
ans = 0

def bfs(y,x,m):
    g = [[None if l[i][j] == '.' else -1 for j in range(w)] for i in range(h)]
    g[y][x] = 0
    q = deque()
    q.append((y,x))

    while q:
        i,j = q.popleft()
        for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
            ni = i+di; nj = j+dj
            if 0 <= ni < h and 0 <= nj < w and g[ni][nj] is None:
                g[ni][nj] = g[i][j] + 1
                q.append((ni,nj))

    return max(max(r) for r in g)

for i in range(h):
    for j in range(w):
        if l[i][j] == '.':
            d = bfs(i,j,l)
            if ans < d:
                ans = d
print(ans)
