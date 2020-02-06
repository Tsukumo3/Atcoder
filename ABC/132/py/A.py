#PythonのCounterでリストの各要素の出現個数をカウント
N = list(input())
import collections
counter = collections.Counter(N)
#print(counter)
ans = "Yes"
for i in counter.values():
    if i != 2:
        ans = "No"
print(ans)
