from fractions import gcd
def lcm(p,q):
    return p*q//gcd(p,q)

n,m = map(int, input().split())
a = list(map(int, input().split()))
x = 1
for i in range(n):
    a[i] = a[i]//2
    x = lcm(x,a[i])
    if x>m:
        print(0)
        exit()
for i in range(n):
    if (x//a[i])%2==0:
        print(0)
        exit()
p = m//x

print(x)
print(p)

if p%2==0:
    ans = p//2
else:
    ans = p//2 +1
print(ans)
