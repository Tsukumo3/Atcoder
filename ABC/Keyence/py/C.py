N,K,S = map(int,input().split())

if K == 0:
    anslist = []
    for i in range(N):
        ramdam = (S+1) % (10**9)
        anslist.append(str(ramdam))
    print(" ".join(anslist))


elif N == K:
    anslist = [str(S) for i in range(N)]
    ansString = " ".join(anslist)
    print(ansString)
    exit()

else:
    if S%2 == 0:
        anslist = [str(S//2) for i in range(K+1)]
        for i in range(N - len(anslist)):
            ramdam = (S+1) % 10**9
            anslist.append(str(ramdam))
        print(" ".join(anslist))

    elif S == 1:
        anslist = []
        for i in range(K):
            item = [str(1)]
            anslist.extend(item)
        for i in range(N - len(anslist)):
            ramdam = (S+1) % 10**9
            anslist.append(str(ramdam))
        print(" ".join(anslist))


    else:
        anslist = []
        t = 1
        for i in range(K-1):
            item = [str(t),str(S-t)]
            anslist.extend(item)
            t += 1
        anslist.append(str(S))
        for i in range(N - len(anslist)):
            ramdam = (S+1) % 10**9
            anslist.append(str(ramdam))
        print(" ".join(anslist))
