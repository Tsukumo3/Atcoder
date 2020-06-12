n = int(input())
A = list(map(int, input().split()))
ans = 0

if n == 0 and A[0] == 1:
    print(1)
    exit()
if n == 0 and A[0] != 1:
    print(-1)
    exit()
if n != 0 and A[0] == 1:
    print(-1)
    exit()


start = 1
way = sum(A)

for i in range(1,n+1):
    start *= 2

    if start < A[i]:
        print(-1)
        exit()
    if start > way:
        start = way

    ans += start
    start -= A[i]
    way -= A[i]
print(ans+1)
