l = list(input())

ans = 0

for i in range(len(l)//2):
    if not l[i] == l[len(l)-i-1]:
        ans+=1
print(ans)
