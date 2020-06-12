def re(time):
    if time == 1:
        print("Yes")
    else:
        re(time-1)

re(10**5)
