'''
ABC065 A - Expired?
https://atcoder.jp/contests/abc065/tasks/abc065_a

賞味期限をX日まで過ぎた食品を食べてもお腹を壊しません。
賞味期限をX+1日以上過ぎた食品を食べると、お腹を壊します。

賞味期限を過ぎずに食べると、おいしく感じます
そうでない場合、おいしく感じません。

高橋君は、賞味期限の A 日前に食品を買ってきて、
買ってから B 日後に食べました。

buy           eat
 |------------|-------|-------|---
 A<-----X
 |----------->B------>B------->B
        |----------|-------|-----|
        X   deli    safe     den

'''

x,a,b = map(int, input().split())

if x >= a+b:
    ans = 'delicious'
elif x <= b:
    ans = 'safe'
else:
    ans = 'dangerous'
print(ans)
