N = int(input())
d_n = list(map(int, input().split()))

answers = [d_n[i]*d_n[j] for i in range(N-1) for j in range(i+1,N)]

#print(answers)

print(sum(answers))
