A = list(map(int, input().split()))
ans1 =  sum(A)

if ans1 > 21:
    print("bust")
else:
    print("win")
