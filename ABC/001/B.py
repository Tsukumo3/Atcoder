m = int(input())

if m < 100:
    vv = 0
    print("00")
elif 100 <= m < 1000:
    vv = m*0.01
    print("0"+str(int(vv)))
elif 1000 <= m <= 5000:
    vv = m*0.01
    print(str(int(vv)))
elif 6000 <= m <= 30000:
    vv = m*0.001+50
    print(int(vv))
elif 35000 <= m <= 70000:
    vv = (m*0.001-30)/5+80
    print(int(vv))
elif 70000 <= m:
    vv = 89
    print(vv)
