'''
【問題概要】
長さ n の正の整数列 a1,a2,…,an と整数 x が与えられる。
整数列の連続する部分列で、その総和が x 以下となるものを数え上げよ
(実際の出題は Q 個のクエリがあって各クエリごとに x が与えられる)。

【制約】

1≤n≤105
1≤Q≤500
1≤ai≤109
1≤xj≤1014

例
n=12
a=(4,6,7,8,1,2,110,2,4,12,3,9)
x=25

12
4 6 7 8 1 2 110 2 4 12 3 9
25
'''
# sys.stdin.readline()
import sys
input = sys.stdin.readline().rstrip()

def syaku_tori(n, a, w):

    res = 0 # count

    sum = 0 # 合計値
    right = 0 #初期値

    for left in range(n):

        while(right < n and sum + a[right] <= w):
            sum += a[right]
            right += 1

        res += (right - left)

        # /* left をインクリメントする準備 */
        if right == left:

            right += 1 #// right が left に重なったら right も動かす
        else:
            sum -= a[left]# // left のみがインクリメントされるので sum から a[left] を引く
    return res

if __name__ == '__main__':
    #n = 12
    #a = [4, 6, 7, 8, 1, 2, 110, 2, 4, 12, 3, 9]
    #w = 25

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    for w in x:
        print(syaku_tori(n, a, w))
