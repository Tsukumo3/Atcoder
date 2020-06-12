    import numpy as np
    #文字列をASCII codeのリストで管理
    S = np.array([ord(i) - 97 for i in input()], dtype=int)
    T = np.array([ord(i) - 97 for i in input()], dtype=int)
    ls = len(S)
    lt = len(T)
    #S[i] == T[j]であれば、i * j行列の[i,j]成分が1となる行列
    equal = np.equal.outer(S,T).astype(int)
    #print(equal)

    dp = [np.zeros(lt + 1,dtype = int)]
    #print(dp)
    for i in range(ls):
      #追加された最後のdp列をx,newDPとする
      x = dp[-1].copy()
      newDP = x.copy()
      #一致しているところで1を足し、そうでないところはそのまま
      newDP[1:] = np.maximum(x[:-1] + equal[i],newDP[1:])
      #dp[i] = i以前のdpの最大値に更新
      np.maximum.accumulate(newDP, out = newDP)
      #最大共通部分を計算するだけなら一列のdp列を使い回せば良いが
      #文字列の復元のために、dp列を追加する
      dp.append(newDP)
      #print(dp)


    ans = ""
    i, j = ls, lt
    #数列の復元と文字列への復元
    while i > 0 and j > 0:
      if S[i - 1] == T[j - 1]:
        ans += chr(S[i - 1] + 97)
        i -= 1
        j -= 1
        continue
      if dp[i][j] == dp[i - 1][j]:
        i -= 1
      else:
        j -= 1

    #リバース
    print(ans[::-1])
