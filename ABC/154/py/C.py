N = int(input())
A = list(map(int,input().split()))

import collections
counter = collections.Counter(A)

for i in list(counter.values()):
    if not i == 1:
        print("NO")
        exit()
print("YES")
