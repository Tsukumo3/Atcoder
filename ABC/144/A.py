ans = -1

try:
    A, B = map(int,input().split())
    if A > 0 and A < 10 and B > 0 and B < 10:
        ans = A*B
except:
    pass

print(ans)
