import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    ans = []
    for w in x:
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
        ans.append(res)
    print(*ans, sep='\n')
