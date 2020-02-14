N, K = map(int,input().split())
P = list(map(int, input().split()))

''' 累積和 '''
cumulative_sum = [P[0]]
for i in range(len(P)-1):
    cumulative_sum.append(cumulative_sum[i] + P[i+1])

#入力
#print(P)
#累積和
#print(cumulative_sum)

#numpy 累積和（高速）
import numpy
res = numpy.cumsum(P)
print(type(res))
#print(res)

''' 最大値探索 O(N-K) '''
#初期値
max = cumulative_sum[K-1]
max_index = 0
for i in range(N-K):
    now = cumulative_sum[K+i] - cumulative_sum[i]
    if max < now:
        max = now
        index = i
#print(max)
#print(max_index)


ans = (max + K)/2
print(ans)
