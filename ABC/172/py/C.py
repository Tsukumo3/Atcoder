from itertools import accumulate

n, m ,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
pile = 0

a_ac = list(accumulate(a))
b_ac = list(accumulate(b))

print(a_ac)
print(b_ac)
