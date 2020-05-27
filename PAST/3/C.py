a,r,n = map(int, input().split())

maxi = pow(10, 9)
ans = a
time = 1
while(time < n):
    ans *= r
    if ans > maxi:
        print("large")
        exit()
    time += 1

print(ans)
