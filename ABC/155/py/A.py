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

Numbers = list(map(int, input().split()))

ans = "No"

import collections
counter = collections.Counter(Numbers)

for i in counter.values():
    if i == 2:
        ans = "Yes"

print(ans)
