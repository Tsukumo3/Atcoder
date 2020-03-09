n,a,b = map(int, input().split())

m = n//(a+b)
s = n%(a+b)
if n < a+b:
    if n <= a:
        print(n)
    else:
        print(a)
else:
    if s <= a:
        print(a*m+s)
    else:
        print(a*m+a)
