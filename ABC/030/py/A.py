s = list(map(int, input().split()))

a = "AOKI"
t = "TAKAHASHI"
d = "DRAW"

m = s[1]/s[0]
n = s[3]/s[2]

if n > m:
    print(a)
elif n < m:
    print(t)
else:
    print(d)
