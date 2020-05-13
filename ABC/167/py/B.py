a, b, c, k = map(int, input().split())
#1 0 -1
t = 0
ans = 0

if a >= k:
    print(k)
else:
    # a < k
    t = k - a

    if b >= t:
        print(a)
    else:
        # b < t
        s = t - b

        print(a-s)
