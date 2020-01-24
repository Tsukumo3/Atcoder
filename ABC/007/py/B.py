N, M = map(int, input().split())
listen = [int(input()) for _ in range(M)]

out_cd = 0
in_cds = [i for i in range(1,N+1)]

#print(in_cds)

for i in range(M):

    #入れ替え
    if listen[i] == out_cd:
        continue
    else:
        cd_index = in_cds.index(listen[i])
        out_cd, in_cds[cd_index] = in_cds[cd_index], out_cd

[print(i) for i in in_cds]
