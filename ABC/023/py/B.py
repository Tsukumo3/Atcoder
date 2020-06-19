n = int(input())
A = [int(input()) for i in range(n)]

#i番目の花は、i>j かつ
#i番目の花の種類とj番目の花の種類が同じ
#になるような j が存在すれば受粉します。
# 1<= Ai <= 10^5

from collections import Counter

c = Counter(A)

ans = 0

for i in c.items():
    if i[1] > 1:
        ans += (i[1] - 1)

print(ans)
