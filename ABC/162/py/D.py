n = int(input())
s = input()

r = s.count("R")
g = s.count("G")
b = s.count("B")
ans = r*g*b

out = 0
t = 1
while(n >= t*2+1):
    for i in range(n-2*t):

        #print(i,i+t,i+2*t)
        #print(s[i],s[i+t],s[i+2*t])

        if s[i] != s[i+t]:
            if s[i+t] != s[i+2*t]:
                if s[i] != s[i+2*t]:
                    ans -= 1
    t+=1

print(ans)
