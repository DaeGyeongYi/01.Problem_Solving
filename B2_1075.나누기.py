from sys import stdin

n = int(stdin.readline())
f = int(stdin.readline())


n = (n//100)*100

for i in range(99):
    if n%f == 0:
        print("%02d"%(n%100))
        break
    n += 1