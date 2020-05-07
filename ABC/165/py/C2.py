"""
https://atcoder.jp/contests/abc165/tasks/abc165_c

C - Many Requirements /

制約
2 <= N <= 10
1 <= N <= 10
1 <= Q <= 50
"""
from collections import deque

deq = deque()
al = []

def solve(n,m,q,x):

    max = 0

    for a_list in al:
        cnt = 0
        for a in x:
            if a_list[ a[1]-1 ] - a_list[ a[0]-1 ] == a[2]:
                cnt += a[3]
        if max < cnt:
            max = cnt

    return max

if __name__ == '__main__':
    n, m, q = map(int, input().split())
    x = [list(map(int, input().split())) for i in range(q)]

    #初期値を設定
    deq.append([1])

    #解になる可能性のある数列を生成
    while(deq):
        item = deq.popleft()
        if len(item) != n:
            for i in range(item[-1],m+1):
                deq.append(item + [i])
        else:
            al.append(item)

    #print(*al, sep='\n')
    ans = solve(n,m,q,x)

    print(ans)
