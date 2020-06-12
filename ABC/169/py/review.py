"""
A: Multiplication 1
https://atcoder.jp/contests/abc169/tasks/abc169_a
subject: Easy
"""
"""
a, b = map(int, input().split())
print(a*b)
"""
"""
B: Multiplication 2
https://atcoder.jp/contests/abc169/tasks/abc169_b
subject: Easy, careless
tips:
* 大きい数字を処理していくのは時間がかかるので, 小さい数字同士をかける.
* 掛け算なので0があるときはすぐに終了させる
* 掛け算を終了してから判定すると時間がかかりすぎるので、for中にjudge
"""
"""
def finish(t):
    print(t)
    exit()

n = int(input())
a = list(map(int, input().split()))

if 0 in a:
    finish(0)

mod = pow(10, 18)
s = 1
for i in range(n):
    s *= a[i]
    if s > mod:
        finish(-1)
else:
    finish(s)
"""
"""
C: Multiplication 3
https://atcoder.jp/contests/abc169/tasks/abc169_c
A×Bの小数点以下を切り捨て、結果を整数として出力
0≤A≤10^15 , 0≤B<10
Aは整数Bは小数第2位まで与えられる

subject: float, decimal:"小数"
tips:
* 2進数では小数を表現しきれない。無限小数のようにある。そこで丸め誤差が発生。
解放1: 小数をfloat(2進数)にしてはだめ、整数(int, str)にしてから計算、再度小数にする
解放2: decimal型(10進数)を用いて計算処理する
"""
"""
#解放1
a, b = input().split()
b = b.replace(".", "")
print(int(a)*int(b)//100)

#解放2
from decimal import Decimal
from math import floor
a, b = input().split()
a = int(a)
b = Decimal(b)
print(floor(a*b))
"""
"""
D: Div Game
https://atcoder.jp/contests/abc169/tasks/abc169_d
subject: 素因数分解, 実装
tips: 素因数分解の関数を手早く実装できるようになる必要がある
"""

"""
E: Count Median
https://atcoder.jp/contests/abc169/tasks/abc169_d
"""

"""
F: Knapsac k for All Subsets
https://atcoder.jp/contests/abc169/tasks/abc169_d
"""
