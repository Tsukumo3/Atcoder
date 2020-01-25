N, K = map(int, input().split())

pow2 = [2**i for i in range(50)]
#print(pow2[-1])
ans = 0

for i in range(1,N+1):
    for j in range(len(pow2)):
        if K <= i*pow2[j]:
            #print(j)
            ans += 1/pow2[j]
            break
ans *= (1/N)
print(ans)
