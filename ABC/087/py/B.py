#ABC087B - Coins
"""全探索でいける？"""
a = int(input())#500
b = int(input())#100
c = int(input())#50
x = int(input())#金額

ans = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if x == (i*500 + j*100 + k*50):
                ans += 1

print(ans)
