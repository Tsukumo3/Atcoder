#  --*-coding:utf-8-*--

MOD =  1000000007

def f(N, A):
    c0 = 0
    c1 = 1

    for i in range(1, N+1):
        c0, c1 = c1, (c0+c1)%MOD

        if i in A:
            c1 = 0

    return c1



def main():
    N,M = map(int, input().split())
    A = set(int(input()) for i in range(M))
    print(f(N, A))


if __name__ == '__main__':
    main()
