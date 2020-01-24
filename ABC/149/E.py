N , M = map(int, input().split())
A_n = list(map(int, input().split()))

length = N

B_n = [A_n[i]+A_n[j] for j in range(length) for i in range(length)]

B_n = sorted(B_n)

ans_list = [B_n.pop() for i in range(M)]

print(sum(ans_list))
