n = int(input())
a = list(map(int, input().split()))
b = [1/i for i in a]
ans = 1/sum(b)
print(ans)
