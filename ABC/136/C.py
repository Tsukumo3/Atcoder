n = int(input())
a = list(map(int, input().split()))

flag = True
for i in range(n-1):
    if a[n-i-2] > a[n-i-1]:
        a[n-i-2]-= 1

    if a[n-i-2] > a[n-i-1]:
        flag = False
        break

print("Yes") if flag else print("No")
