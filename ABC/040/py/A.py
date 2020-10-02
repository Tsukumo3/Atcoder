"""
ABC039 A - Takahashi chokutai
https://atcoder.jp/contests/abc040/tasks/abc040_a
"""
n, x = map(int, input().split())

if n%2 == 0 : # even
    if n-x >= n/2 : # 6 - 2
        ans = x-1
    else: # 6- 4
        ans = n-x
else : # odd
    if n-x >= n/2 : # 5 - 2
        ans = x-1
    else: # 5 - 4
        ans = n-x
print(ans)
