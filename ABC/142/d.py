import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def cf(x1,x2):
    cf=[]
    for i in range(2,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf

a,b = map(int, input().split())

#commonDivisor
cd = []
cd.extend(cf(a,b))

length = len(cd)
ans = 1

for i in range(length):
    if (is_prime(cd[i])):
        ans += 1

print(ans)
