s = input()
ans = 0
left = 0
right = 4
while(left <= len(s)-2):
    while(right <= len(s)+1):
        #print(left, right-1)
        right += 1
        num = int(s[left:right])
        if num % 2019 == 0:
            #print(left, right-1)
            ans += 1
            left = right - 2
            break
    left+=1
    right = left + 4
print(ans)
