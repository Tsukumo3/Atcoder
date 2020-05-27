import os

for i in range(20):
    filename = chr(ord("A") + i) + ".py"
    f = open(filename,'w')
    f.write('hoge\n')
    f.close()
