A,B,C,D = map(int, input().split())

_range = list(range(A,B+1))

ans_list = []

for item in _range:
    if not item % C == 0 and not item % D == 0:
        ans_list.append(item)

print(len(ans_list))
