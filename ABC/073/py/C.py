#PythonのCounterでリストの各要素の出現個数をカウント

N = int(input())
Numbers = [int(input()) for _ in range(N)]


import collections

counter = collections.Counter(Numbers)

#print(counter)

ans = 0

for i in counter.values():
    if i % 2 == 1:
        ans += 1

print(ans)
