W, H, x, y = map(int, input().split())

#正方形なら複数　これも面積半分?
#長方形なら一つ 点対称の線を引けば面積半分にできる

if W/2 == x and H/2 == y:
    print(W*H/2, 1)
else:
    print(W*H/2, 0)
