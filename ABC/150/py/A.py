A,B = map(int, input().split())

ans  = 500*A - B

if ans >= 0:
    print("Yes")
else:
    print("No")
