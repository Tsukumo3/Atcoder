import collections

q = collections.deque()
n, x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

q.append((0, 0, 0))

move = ((1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1))

x_max, y_max = max(0,x), max(0,y)
x_min, y_min = min(0,x), min(0,y)

for i in l:
    x_min = min(x_min, i[0])
    x_max = max(x_max, i[0])
    y_min = min(y_min, i[1])
    y_max = max(y_max, i[1])

x_max += 1
y_max += 1
x_min -= 1
y_min -= 1

while q:
    i, j, t = q.popleft()

    if (i, j) == (x, y):
        print(t)
        exit()

    for di, dj in move:
        ni , nj = i + di, j + dj
        if not [ni, nj] in l and x_min <= i <= x_max and y_min <= j <= y_max:
            q.append((ni, nj, t+1))
else:
    print(-1)
