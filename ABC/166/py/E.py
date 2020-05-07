n = int(input())
a = list(map(int, input().split()))

L = {}
R = {}

for i in range(n):
    if i + a[i] in L:
        L[i + a[i]] = L[i + a[i]] + 1
    else:
        L[i + a[i]] = 1

    if i - a[i] in R:
        R[i - a[i]] = R[i - a[i]] + 1
    else:
        R[i - a[i]] = 1

#print(L,R,sep="\n")
ans = 0
for key in L.keys():
    if key in R:
        #print(L[key], R[key])
        ans += L[key] * R[key]
print(ans)

"""
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if abs(i-j) == a[i]+a[j]:
            ans += 1
print(ans)
"""
