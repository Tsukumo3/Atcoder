A, B, K = map(int,input().split())

if(K >= A):
    K -= A
    A = 0
    if(K >= B):
        B = 0
    else:
        B -= K
else:
    A -= K

print(str(A) + " " + str(B))
