from itertools import accumulate

n,  h = map(int, input().split())
a = [int(input()) for i in range(n)]

s = [0] + list(accumulate(a))
for i in range(n-3):
    if (s[i+3] - s[i]) < h:
        print(i+3)
        exit()
print(-1)
