n = int(input())
a = list(map(int, input().split()))

flag = True
for i in range(n-1):
    if a[i] > a[i+1]:
        a[i]-=1
print(a)
for i in range(n-1):
    if a[i] > a[i+1]:
        flag = False
        break
print(a)
print("Yes") if flag else print("No")
