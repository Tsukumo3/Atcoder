"""
C - Average Length
https://atcoder.jp/contests/abc145/tasks/abc145_c
"""
import itertools

n = int(input())
point = [list(map(int, input().split())) for i in range(n)]

distances = []

for i in range(n-1):
    for j in range(i+1, n):
        xi, yi = point[i]
        xj, yj = point[j]

        d = pow(pow(xi - xj, 2) + pow(yi - yj, 2), 0.5)
        distances.append(d)

ans = 2* sum(distances) / n

print(ans)
