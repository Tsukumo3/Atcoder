'''
提出情報
提出日時	2019-05-26 21:02:21
問題	B - Guidebook
ユーザ	nagiss イエローコーダー
言語	Python3 (3.4.3)
得点	200
コード長	160 Byte
結果
実行時間	17 ms
メモリ	3060 KB

'''

N = int(input())
a = []
for i in range(N):
    N, K = input().split()
    K = int(K)
    a.append([N, -K, i+1])　#マイナスくるとちゃんとソートできる・・・
a.sort()
for a_ in a:
    print(a_[2])
