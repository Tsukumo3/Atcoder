A, B = map(int, input().split())

_sum = A + B
_sub = A - B
_mul = A * B

_list = [_sum,_sub,_mul]

print(max(_list))
