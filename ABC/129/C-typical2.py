memo = {}

def starsFib(n,a):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    elif n in a:
        return 0
    else:
        fib = (starsFib(n-1,a) + starsFib(n-2,a))% 1000000007
        memo[n] = fib
        return memo[n]

def run():
    n,m = map(int, input().split())
    a = [int(input()) for i in range(m)]

    all = starsFib(n,a)

    ans = all % 1000000007

    print(ans)

if __name__ == '__main__':
    run()
