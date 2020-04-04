import collections

#メモ
memo = {}
def combination(n, a, mod):

    if (n,a) in memo:
        return memo[(n,a)]

    x = 1
    y = 1
    for i in range(a):
        x = x * (n-i)%mod
        y = y * (a-i)%mod

    ans = x * pow(y, mod-2, mod)%mod

    memo[(n, a)] = ans
    return ans

def solve(i):



n = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)

for i in a:
