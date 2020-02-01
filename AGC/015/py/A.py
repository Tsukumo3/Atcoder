'''
制約
1≦N,A,B≦10^9
N  = 1の時ABもない

A < B
B < A
'''
N, A, B = map(int,input().split())

if A > B:
    print(0)
    exit()
elif N == 1 and A != B:
    print(0)
    exit()
else:
    min_sum = A * (N - 1) + B
    max_sum = A + B * (N - 1)

    ans = max_sum - min_sum + 1

    print(ans)
