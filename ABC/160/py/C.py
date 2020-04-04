k, n = map(int, input().split())
a = list(map(int, input().split()))

x = 0
index = 0

for i in range(n-1):
    if x < a[i+1] - a[i]:
        x = a[i+1] - a[i]
        index = i

if x < k-a[-1]+a[0]:
    x = k-a[-1]+a[0]

print(k - x)
