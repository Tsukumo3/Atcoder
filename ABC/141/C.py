n,k,q = map(int,input().split())
a_n = [int(input()) for i in range(q)]

p_n = [k-q for i in range(n)]

for a_i in a_n:
    p_n[a_i-1] += 1

[print("Yes") if p_i > 0 else print("No") for p_i in p_n]
