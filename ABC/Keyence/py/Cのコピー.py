N,K,S = map(int,input().split())

anslist = []

if S < 10**9:
    for i in range(K):
        anslist.append(S)
    for i in range(N-K):
        anslist.append(S+1)
elif S == 10**9:
    for i in range(K):
        anslist.append(S)
    for i in range(N-K):
        anslist.append(1)

ansString = [str(i) for i in anslist]

print(" ".join(ansString))
