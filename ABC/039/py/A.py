"""
ABC039 A - Takahashi chokutai
https://atcoder.jp/contests/abc039/tasks/abc039_a
"""

a, b, c = map(int, input().split())
ans = a*b*2 + a*c*2 + b*c*2
print(ans)
