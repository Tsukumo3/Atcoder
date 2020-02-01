N,K = map(int,input().split())
H = list( map(int,input().split()))

time = 0

H.sort()

if N < K:
    K = N

for i in range(K):
    H[-i-1] = 0

print(sum(H))
