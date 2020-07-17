n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for i in range(q)]

from collections import deque

q = deque()

for i in bc:
    q.append(i)

while (len(q) != 0):
    now = q.popleft()

    for i in range(len(q)):
        if now[1] == q[i][0]
