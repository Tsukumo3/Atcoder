n = input()
a = list(map(int, input().split()))

s = 1
mod = pow(10, 18)

if 0 in a:
    print(0)
    exit()

for i in a:
    s = s*i
    if s > mod:
        print(-1)
        exit()
else:
    print(s)
