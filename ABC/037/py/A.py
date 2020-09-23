"""
ABC037 A - Manju
https://atcoder.jp/contests/abc037/tasks/abc037_a
"""

a, b, c = map(int, input().split())
min = a if a < b else b
ans = c//min

print(ans)
