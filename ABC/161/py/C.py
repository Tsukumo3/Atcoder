n, k = map(int, input().split())

h = n%k

if h >= k/2:
    print(abs(h-k))
else:
    print(h)
