'''
abc063 A - Restricted
https://atcoder.jp/contests/abc063/tasks/abc063_a
'''

a, b = map(int, input().split())
ans = a+b if a+b < 10 else 'error'
print(ans)
