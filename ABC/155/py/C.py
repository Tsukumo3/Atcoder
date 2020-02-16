'''
n = int(input())
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [int(input()) for i in range n]
p = [list(map(int, input().split()))]

a = input()
a, b = input().split()
a = [input() for i in range n]
'''
n = int(input())
a = [input() for i in range(n)]

ans = []

import collections
counter = collections.Counter(a)

max_h = max(counter.values())


for i in counter.items():
    #print(i)
    if i[1] == max_h:
        ans.append(i[0])
    else:
        pass

ans.sort()

[print(i) for i in ans]
