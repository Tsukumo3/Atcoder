n = input()
print(len(n))
n_list = [int(i) for i in n]

ans = 0

'''
10^100+1の効果

'''

for i in range(n):
    #print(type(c))
    if i >= 0 and i <= 5:
        ans += i
    else:
        ans += (11 - i)

print(ans)
