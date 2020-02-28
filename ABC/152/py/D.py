N = int(input())
N_str = list(str(N))
length = len(str(N))

#1<=k<=Nで 先頭がiで末尾がjの総和
c = [[0]*9 for i in range(9)]
'''
#C(i,j)を求めるのは無理

def count(i, j):
    pass

for i in range(9):
    for j in range(9):
        c[i][j] = count(i, j)
'''

for i in range(1, N+1):
    s = str(i)
    if s[0] == "0" or s[-1] == "0":continue
    c[int(s[0])-1][int(s[-1])-1] += 1

ans = 0
for i in range(9):
    for j in range(9):
        ans += c[i][j] * c[j][i]

print(ans)
