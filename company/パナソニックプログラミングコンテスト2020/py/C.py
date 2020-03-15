a, b, c = map(int, input().split())
if 0 < pow((c-a-b),2) - 4*a*b and c-a-b > 0:
    print("Yes")
else:
    print("No")
