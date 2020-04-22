"""
C - Average Length
https://atcoder.jp/contests/abc145/tasks/abc145_c
"""
import itertools

n = int(input())
point = [list(map(int, input().split())) for i in range(n)]

distances = {}

for i in range(n-1):
    for j in range(i+1, n):
        xi, yi = point[i]
        xj, yj = point[j]

        d = pow(pow(xi - xj, 2) + pow(yi - yj, 2), 0.5)
        distances[(i, j)] = d
        distances[(j, i)] = d

next = itertools.permutations(range(n))

all = 0

for root in next:
    for i in range(len(root)-1):
        all += distances[(i, i+1)]

bunbo = 1
for i in range(1,n+1):
    bunbo *= i
print(all/bunbo)
