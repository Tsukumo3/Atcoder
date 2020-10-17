'''
ABC071 A - Meal Delivery
https://atcoder.jp/contests/abc071/tasks/abc071_a
'''

x, a, b = map(int, input().split())

if abs(x-a) > abs(x-b):
    ans = 'B'
else:
    ans = 'A'
print(ans)
