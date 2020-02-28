import numpy as np

def combination(n, a):
    mod = pow(10, 9)+7
    x = 1
    y = 1
    for i in range(a):
        x = x * (n-i)%mod
        y = y * (a-i)%mod
    return x * pow(y, mod-2, mod)%mod

x, y = map(int, input().split())

if (x + y)%3 != 0:
    print(0)
else:
    A = np.matrix([
        [2, 1],
        [1, 2]
        ])
    B = np.matrix([
        [x],
        [y]
        ])
    #ans = np.linalg.inv(A)*B
    ans1 = np.linalg.solve(A,B)
    n, m = int(ans1[0]), int(ans1[1])
    ans2 = combination(n+m, n)
    print(ans2)
