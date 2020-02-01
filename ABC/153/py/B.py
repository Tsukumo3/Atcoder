H,N = map(int,input().split())
A = list( map(int,input().split()))

ans = H -sum(A)

if ans <= 0:
    print("Yes")
else:
    print("No")
