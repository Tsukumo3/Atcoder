K, X = map(int, input().split())

_range = list(range(X-(K-1),X+K))

#print(_range)

#ans = " ".join([str(n) for n in _range])

[print(str(i) ,end=' ') for i in _range]
