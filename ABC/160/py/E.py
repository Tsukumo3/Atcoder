x, y , a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse = True)
q.sort(reverse = True)
r.sort(reverse = True)

p_point = 0
q_point = 0
r_point = 0

ans = 0

for i in range(x):

    try:

        if p[p_point] > r[r_point]:
            ans += p[p_point]
            p_point += 1
        else:
            ans += r[r_point]
            r_point += 1
    except:
        ans += r[r_point]
        r_point += 1


for i in range(y):
    try:
        if q[q_point] > r[r_point]:
            ans += q[q_point]
            q_point += 1
        else:
            ans += r[r_point]
            r_point += 1
    except:
        ans += r[r_point]
        r_point += 1
print(ans)
