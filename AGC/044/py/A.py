def divisors(n):

    div_list=[]

    c = str(n)
    c1 = int(c[-1])
    if c1%2==0:
        div_list.append(2)

    if c1 == 0 or c1 == 5:
        div_list.append(5)

    c_sum = sum([int(i) for i in c])

    if c_sum%3 ==0:
        div_list.append(3)

    return div_list

def solve(n, div, l):
    #print(n,div,l)
    div.sort(reverse=True)
    d = [0,0,0]
    adict = {2:0, 3:1, 5:2}
    n = float(n)
    for i in range(len(div)):
        index = adict[div[i]]
        while(n.is_integer()):
            n /= div[i]
            d[index] += 1
            #print(n,div[i])
        n*= div[i]
        d[index] -= 1

    print(d)

    if d[0] > 0:
        print(l[1]*d[0] + l[2]*d[1] + l[3]*d[2], l[1]*(d[0]-1) + l[2]*d[1] + l[3]*d[2] + l[4])
        return min(l[1]*d[0] + l[2]*d[1] + l[3]*d[2], l[1]*(d[0]-1) + l[2]*d[1] + l[3]*d[2] + l[4])
    else:
        return l[1]*d[0] + l[2]*d[1] + l[3]*d[2]


t = int(input())
l = [list(map(int, input().split())) for i in range(t)]

for i in range(t):
    div = divisors(l[i][0])
    #print(l[i][0], div)

    if len(div) == 0:
        div = divisors(l[i][0]+1)
        mini = solve(l[i][0]+1, div, l[i])
        #print(l[i][0]+1, div)

        div = divisors(l[i][0]-1)
        mini = min(solve(l[i][0]-1, div, l[i]), mini)
        mini += l[i][4]*2
        print(mini)
        #print(l[i][0]-1, div, mini)

    else:
        mini = min(solve(l[i][0], div, l[i]), mini)
        print(mini +l[i][4])
    print()
