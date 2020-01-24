import itertools

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

seq = itertools.permutations(range(1,N+1))
listseq = list(seq)
tupleA = tuple(A)
tupleB = tuple(B)

indexA = listseq.index(tupleA) + 1
indexB = listseq.index(tupleB) + 1

ans = abs(indexA - indexB)

print(ans)
