div = 10**9 + 7
ans = 0

N = int(input())
A = list(map(int, input().split()))

memo = {}

for i in range(N):
    for j in range(i+1,N):
        #print(str(i) + " : " + str(j))
        if (A[i],A[j]) in memo:
            ans += memo[A[i],A[j]]

        else:
            a = A[i]^A[j]
            memo[A[i],A[j]] = a
            ans+= a

print(ans%div)
