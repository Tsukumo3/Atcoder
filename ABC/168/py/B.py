k = int(input())
s = input()

if len(s) > k:
    ans = s[:k] + "..."
else:
    ans = s

print(ans)
