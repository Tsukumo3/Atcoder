A = []
for i in range(3):
    l = list(map(int, input().split()))
    A.extend(l)
N = int(input())
B = [int(input()) for i in range(N)]

bingo = [False for i in range(9)]

for i in range(N):
    if B[i] in A:
        a_index = A.index(B[i])
        bingo[a_index] = True

ans = False

#横３pattern
#if all([A[i*3], A[i*3 + 1], A[i//3 + 2] for i in range(3)]):
for i in range(3):
    if all([bingo[i*3], bingo[i*3 + 1], bingo[i*3 + 2]]):
        ans = True
#縦３pattern
#if all([A[i*3 + i], A[(i+1)*3 + i], A[(i+1)*3 + i] for i in range(3)]):
for i in range(3):
    if all([bingo[i], bingo[3 + i], bingo[6 + i]]):
        ans = True
#斜め2pattern
if all([bingo[0], bingo[4], bingo[8]]) or all([bingo[2], bingo[4], bingo[6]]):
    ans = True
print("Yes") if ans else print("No")
