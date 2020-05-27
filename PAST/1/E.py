def follow(g, a, b):
    g[a-1][b-1] = "Y"
    return g

def follow_return(g, a, n):
    for i in range(n):
        if g[i][a-1] == "Y":
            g[a-1][i] = "Y"

    return g

def follow_follow(g, a, n):

    follow_list = []

    for i in range(n):
        if g[a-1][i] == "Y":

            for j in range(n):
                if g[i][j] == "Y":
                    follow_list.append(j)

    for i in follow_list:
        if i != a-1:
            g[a-1][i] = "Y"

    return g



if __name__ == '__main__':

    n,q = map(int, input().split())
    s = [input().split() for i in range(q)]

    g = [["N" for i in range(n)] for j in range(n)]

    for i in s:
        if i[0] == "1":
            g = follow(g,int(i[1]), int(i[2]))
        elif i[0] == "2":
            g = follow_return(g, int(i[1]), n)
        elif i[0] == "3":
            g = follow_follow(g, int(i[1]), n)

    for i in g:
        print(*i, sep='')
