n = int(input())

if n == 1:
    print('{0:.10f}'.format(1))
else:
    a = n%2
    if a == 1:
        amari = ((n-1)/2 +1)/n
        print('{0:.10f}'.format(amari))
    else:
        print('{0:.10f}'.format(0.5))
