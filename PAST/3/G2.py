import collections
q = collections.deque()
n, x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

q.append((0, 0, 0))

move = ((1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1))

while q:
    i, j, t = q.popleft()

    if (i, j) == (x, y):
        print(t)
        exit()

    next = []
    for di, dj in move:
        ni , nj = i + di, j + dj
        next.append([ni, nj])

    flag = True
    for i in next:
        if not i in l:
            flag = False

    if flag:
        for ni, nj in move:
            q.append((ni, nj, t+1))
    else:
        for ni, nj in move:
            now = abs(i - x)**2 + abs(j - y)**2
            nex = abs(ni - x)**2 + abs(nj - y)**2
                #print("next", ni, nj, now, nex, now-nex, now >= nex)
            if now - nex >= 0:
                q.append((ni, nj, t+1))
else:
    print(-1)
