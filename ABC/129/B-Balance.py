n = int(input())
w = list(map(int, input().split()))

s1 = 0
s2 = 0
dif = 0
ans = 1000000

for i in range(n):

    s1 = sum(w[:i+1])
    s2 = sum(w[i+1:])
    dif = abs(s1 - s2)


    #print("S1 : " + str(s1) + " S2 : " + str(s2) + " abs : " + str(dif))

    if ans > dif:
        ans = dif

    if ans < dif:
        break

    s1 = 0
    s2 = 0

print(ans)
