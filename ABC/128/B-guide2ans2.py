'''
提出情報
提出日時	2019-11-14 21:47:03
問題	B - Guidebook
ユーザ	ralt
言語	Python3 (3.4.3)
得点	200
コード長	194 Byte
結果
実行時間	17 ms
メモリ	3060 KB
https://atcoder.jp/contests/abc128/submissions/8433463
'''

n = int(input())
a = []
for i in range(1, n+1):
    b,c = input().split()
    a.append([i,b,int(c)*-1])
a = sorted(a, key=lambda x: (x[1], x[2]))
for i in range(n):
    print(a[i][0])
