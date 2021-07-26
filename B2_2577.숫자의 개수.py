import sys
mul = 1
count=[0]*10

for _ in range(3):
     num = int(sys.stdin.readline())
     mul *= num

for i in str(mul):
    count[int(i)] += 1

for i in range(len(count)):
    print(count[i])