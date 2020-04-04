def combination(n, a, mod):
    x = 1
    y = 1
    for i in range(a):
        x = x * (n-i)%mod
        y = y * (a-i)%mod

        #x *= (n-i)
        #x %=mod
        #y *= (a-i)
        #y %=mod
    return x * pow(y, mod-2, mod)%mod

n, m = map(int, input().split())

ans = combination(n,2,pow(10,9)+7) + combination(m, 2, pow(10,9)+7)
print(ans)
