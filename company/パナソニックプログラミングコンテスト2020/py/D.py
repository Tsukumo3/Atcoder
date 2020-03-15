n = int(input())

s = ['' for i in range(n)]
def dfs(k, c):
    if k == n:
        print("".join(s))
        return
    for i in range(c):
        s[k] = chr(i+ord('a'))
        dfs(k+1, c)
    s[k] = chr(c+ord('a'))
    dfs(k+1, c+1)

dfs(0, 0)
