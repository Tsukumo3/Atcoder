from collections import deque

''' input '''
n = int(input())
tests = []
for i in range(n):
    A = int(input())
    say = [list(map(int, input().split())) for i in range(A)]
    tests.append(say)

''' 1とNoneの部分をカウントする '''
def count_one(a_list):
    count = 0
    for i in a_list:
        if i != 0:
            count += 1
    return count

''' 証言をチェックする '''
def judge(r, go): # rは最初に正しいと仮定した人
    # kindの人数
    num = 0
    # 証言か正しいかどうをチェックする表
    case = r
    print(case)
    # この組み合わせが正しいかどうかをチェックする
    this = True

    print("go:", go)

    # 証言を元に一つ一つ精査していく
    while go:
        say = go.popleft()
        # 食い違いの証言がある時、これは増え成立であるので
        if (case[say[0]-1] == 0 and say[1] == 1) or (case[say[0]-1] == 1 and say[1] == 0):
            this = False
            print("False case")
            break
    print(case)
    if this:

        # 1 のkindの人数を数える
        num = count_one(case)

    return num

''' 全bit探索 '''
def all_bit_search():
    # 最大値
    max = 0
    # 全bit探索
    for i in range(1,2**n):
        go = deque() # 1が立つものを集めるqueue
        for j in range(n):
            if (i >> j) & 1:
                go.extend(tests[j])
        # 証言が正しいか判断する
        r = list(bin(i)[2:]s.zfill(3))
        now = judge(r, go)
        if max < now:
            max = now
    return max


# プログラムを始める
ans = all_bit_search()
print(ans)
