n = input()
ans = True
for i in range(len(n)//2):
    if n[i] != n[-i-1]:
        ans = False
print("YES") if ans else print("NO")
