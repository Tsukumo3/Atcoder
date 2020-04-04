k = int(input())
time = 1

dp0 = [1]#0,9
dp1 = [8]#1~8
p = [9]

for i in range(100):
    dp0.append(dp0[i]*2 + 2)
    dp1.append(dp1[i]*3 - 2)
    p.append(dp0[i+1] + dp1[i+1] + p[i])

    if p[len(p)-1] > k:
        break

#print(len(p))
s = k - p[len(p)-2]
w = [0]*len(p)
print(s,w)
