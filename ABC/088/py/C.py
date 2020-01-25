P = [list(map(int,input().split())) for i in range(3)]
#[print(i) for i in P]
#C11を取得
c_11 = P[0][0]
#引き算する
for i in range(3):
    for j in range(3):
        P[i][j] -= c_11

#[print(i) for i in P]

A_1 = 0
A_2 = P[1][0]
A_3 = P[2][0]
B_1 = 0
B_2 = P[0][1]
B_3 = P[0][2]

Flag = "Yes"

if not A_2 + B_2 == P[1][1]:
    Flag = "No"
if not A_2 + B_3 == P[1][2]:
    Flag = "No"
if not A_3 + B_2 == P[2][1]:
    Flag = "No"
if not A_3 + B_3 == P[2][2]:
    Flag = "No"

print(Flag)
