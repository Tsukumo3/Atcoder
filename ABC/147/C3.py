''' input '''
n = int(input())
tests = []
for i in range(n):
    A = int(input())
    say = [list(map(int, input().split())) for i in range(A)]
    tests.append(say)

def solve():
    max = 0
    # 同じリストを繰り返し使用: 引数repeat イテラブルオブジェクトを繰り返し使用して直積を生成する。
    from itertools import product
    bits = product([0, 1], repeat=n)
    #print(*bits, sep='\n')

    for x in bits:
        flag = 0
        for j in range(N):
            if x[j] == 1:
                for a, b in tests:
                    if b != x[a-1]:
                        flag = 1
                        break
            if flag == 1:
                break
        else:
            tmp = sum(x)



    return 0


ans = solve()
print(ans)
