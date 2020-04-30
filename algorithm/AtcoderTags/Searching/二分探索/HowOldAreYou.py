'''
年齢当てゲームの実装
0 歳以上 10*9 歳未満であることはわかっている
A さんの年齢をズバリ当てる！

以下の実装のキーとなる変数 left, right についてですが、

x = left は「A さんの年齢は x 歳以上である」という条件を満たす
x = right は「A さんの年齢は x 歳以上である」という条件を満たさない
という状態を常に保つようにしています。言い換えれば、
A さんの年齢の候補が常に left 歳以上 right 歳未満となるように定めています。
初期状態は left = 20, right = 36 と 16 歳分の幅がありますが、
質問を通して狭めて行きます。
終了状態では right - left = 1 となっていて、
A さんは left 歳以上 right 歳未満なので left 歳で確定します。

なお、上の年齢当てゲームでは簡単のために
right - left が 2 の冪乗 (2^4 = 16)
になるようにしていましたが、そうでなくても下の実装はきちんと動作します。
例えば left = 0, right = 100 としてもきちんと動作します
(その場合は最大で 7 回の質問で当てます)。
'''

def binarySearch(key):
    left = -1
    right = pow(10,9)+1

    while(right - left > 1):

        mid = left + (right - left)//2
        print(mid)
        if key == mid:
            return mid
        elif key > mid:
            left = mid
        elif key < mid:
            right = mid

    return -1

if __name__ == '__main__':
    print((binarySearch(10**6+41)))
    print("- * - * - * - * - * - ")
    print((binarySearch(10**2+41)))
