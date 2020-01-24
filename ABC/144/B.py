A = int(input())

kk = [i*j for i in range(1,10) for j in range(1,10)]

ans = "No"

if A in kk:
    ans = "Yes"

print(ans)
