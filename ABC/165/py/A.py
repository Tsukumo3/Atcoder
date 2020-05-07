k = int(input())
a, b = map(int, input().split())
ans= 0

for i in range(a,b+1):
    if i % k == 0:
        print("OK")
        exit()
else:
    print("NG")
