N = int(input())
S = list(input())

ans = "No"

center = N//2

a1 = "".join(S[:center])
a2 = "".join(S[center:])

if a1 == a2:
    ans = "Yes"

print(ans)
