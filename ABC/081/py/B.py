n = int(input())
a = list(map(int, input().split()))
ans = 0
def even(x):
    return x%2 == 0

def loop(ans, a):
    while(True):
        #print(a)
        for i in range(n):
            if even(a[i]):
                a[i] = a[i]//2
            else:
                return ans
        ans += 1
    return ans

ans = loop(ans, a)
print(ans)
