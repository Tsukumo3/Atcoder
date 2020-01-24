#払う
N = int(input())
#１円の枚数
A = int(input())

pay = N%500

if pay <= A:
    print("Yes")
else:
    print("No")
