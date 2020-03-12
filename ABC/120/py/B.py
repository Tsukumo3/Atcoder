a, b, k = map(int, input().split())
c = []
for i in range(1, min(a,b)+1):
    if a%i == 0 and b %i == 0:
        c.append(i)
print(c[-k])

'''
A,Bの両方割り切れる
なら範囲は　　1 ~ min(A, B)
'''
