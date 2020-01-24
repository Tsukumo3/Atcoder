N = int(input())
s = ["".join(sorted(list(input()))) for i in range(N)]

print(s)

#出現文字列
sdict = {}

ans = 0

for i in range(N):

    s_i = str(s[i])

    if s_i in sdict:
        #組み合わせが増えるので
        sdict[s_i]+= 1
        continue

    for j in range(i+1,N):
        sdict[s_i] = 1

for i in sdict.values():
    ans += i*(i-1)//2

print(ans)
