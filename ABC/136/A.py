A,B,C = map(int, input().split())

space = A - B

ans = C - space

ans = ans if ans >= 0 else 0

print(ans)
