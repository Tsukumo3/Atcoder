def end():
    print("No")
    exit()

n, a, b, c = map(int, input().split())
s = [input() for i in range(n)]
log = []

for i in range(n):
    if s[i] == "AB":
        # コーナーケース
        if a == 1 and b == 1:
            # aが重複 最後はどっちでもいいので
            if i == n-1 or s[i+1] == "AB" or s[i+1] == 'AC':
                a += 1
                b -= 1
                log.append("A")
            # Bが重複
            else:# "BC"
                a -= 1
                b += 1
                log.append("B")
        elif a == 0 and b == 0:
            end()
        else:
            if a>=b:
                a -= 1
                b += 1
                log.append("B")
            else:
                a += 1
                b -= 1
                log.append("A")

    elif s[i] == "AC":
        # コーナーケース
        if a == 1 and c == 1:
            # aが重複
            if i == n-1 or s[i+1] == "AC" or s[i+1] == 'AB':
                a += 1
                c -= 1
                log.append("A")
            # Cが重複
            else:# "BC"
                c += 1
                a -= 1
                log.append("C")
        elif a == 0 and c == 0:
            end()
        else:
            if a>=c:
                a -= 1
                c += 1
                log.append("C")
            else:
                a += 1
                c -= 1
                log.append("A")
    else:#BC
        # コーナーケース
        if c == 1 and b == 1:
            # Bが重複
            if i == n-1 or  s[i+1] == "BC" or s[i+1] == 'AB':
                c -= 1
                b += 1
                log.append("B")
            # Cが重複
            else:# "AC"
                c += 1
                b -= 1
                log.append("C")
        elif b == 0 and c == 0:
            end()
        else:
            if b>=c:
                b -= 1
                c += 1
                log.append("C")
            else:
                b += 1
                c -= 1
                log.append("B")
else:
    print("Yes")
    print(*log, sep='\n')
