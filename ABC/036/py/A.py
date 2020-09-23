"""
ABC036 A-tea
https://atcoder.jp/contests/abc036/tasks/abc036_a
"""

a, b = map(int, input().split())
ex = 1 if b%a > 0 else 0
ans = b//a + ex

print(ans)
