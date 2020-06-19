"""
子供：A円/人
大人：B円/人
合計人数がK人以上の団体なら一人当たりC円引き
子供、大人=s,t
"""

a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

ans = a * s + b * t

if s+t >= k:
    ans -= (s+t)*c

print(ans)
