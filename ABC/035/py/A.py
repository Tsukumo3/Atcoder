"""
A - TV
https://atcoder.jp/contests/abc035/tasks/abc035_a
"""
w, h = map(int, input().split())

# w*3 = h*4 or w*9 = h*16

if w*3 == h*4:
    print("4:3")
else:
    print("16:9")
