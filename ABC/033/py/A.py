"""
A - 暗証番号
https://atcoder.jp/contests/abc033/tasks/abc033_a
"""

txt = input()

for i in range(1, len(txt)):
    if txt[0] != txt[i]:
        print("DIFFERENT")
        break
else:
    print("SAME")

exit()
