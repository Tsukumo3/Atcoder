def solve(n,m):
    for i in range(n-1):
        for j in range(i+1,n):
            num = int(s[i:j+1])
            if num % 2019 == 0:
                print(i,j)
                return i, j
s= input()
ans = 0

solve(len(s), )

print(ans)
