x = input()
start = ord("A")
time = 1
while(True):
    if chr(start) == x:
        print(time)
        exit()
    time += 1
    start += 1
