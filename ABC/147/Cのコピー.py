n = int(input())
tests = []

def count_one(a_list):
    count = 0
    for i in a_list:
        if i == 1:
            count += 1
    return count

for i in range(n):
    A = int(input())
    say = [list(map(int, input().split())) for i in range(A)]
    tests.append(say)

max = 0

for i in range(2**n):
    go = []
    for j in range(n):
        if (i >> j) & 1:
            go.extend(tests[j])

    this_case = [None for i in range(n)]
    this = True

    #if len(go) == 0: continue
    print(i,"go : ", go)
    for k in range(len(go)):
        if this_case[go[k][0]-1] == None:
            this_case[go[k][0]-1] = go[k][1]
        elif this_case[go[k][0]-1] == 0 and go[k][1] == 1:
            this = False
            print("False case")
            break
        elif this_case[go[k][0]-1] == 1 and go[k][1] == 0:
            this = False
            print("False case")
            break

    if this:
        print(this_case)
        ans = count_one(this_case)
        if ans > max:
            max = ans

print(max)
