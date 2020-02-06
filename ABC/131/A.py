S = input()
buffer = S[0]

ans = "Good"

for i in range(1,len(S)):
    #print(S[i])
    if buffer == S[i]:
        ans = "Bad"
        break

    buffer = S[i]

print(ans)
