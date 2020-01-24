from scipy.special import comb

N = int(input())
s = [sorted(list(input())) for i in range(N)]
s.sort()

#[print(i) for i in s]

#同値関係 推移律を適用する
equals = []

ans = 0

for i in range(N):

    if i in equals:
        continue

    for j in range(i+1,N):
        if s[i] == s[j]:
            equals.append(j)
            ans+=1

    if len(equals)>1
        ans+=comb(len(equals), 2, exact=True)

if not ans == 0:
    print(ans)
else:
    print(0)
