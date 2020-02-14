N, K = map(int,input().split())
P = list(map(int, input().split()))

''' 累積和 '''
cumulative_sum = [P[0]]　#初期値
for i in range(len(P)-1):
    cumulative_sum.append(cumulative_sum[i] + P[i+1])

''' 最大値探索 O(N-K) '''
max = cumulative_sum[K-1]　#初期値
max_index = 0
for i in range(N-K):
    now = cumulative_sum[K+i] - cumulative_sum[i]
    if max < now:
        max = now
        index = i

ans = (max + K)/2
print(ans)
