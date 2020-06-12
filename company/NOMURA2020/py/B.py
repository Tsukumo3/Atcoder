T = input()
ans = []
for i in range(len(T)):
    if T[i] == "?":
        ans.append("D")
    else:
        ans.append(T[i])
print(*ans,sep="")
