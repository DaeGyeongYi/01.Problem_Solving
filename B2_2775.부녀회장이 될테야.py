t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    zero_floor = [x for x in range(1, n+ 1)]
    for k in range(k):
        for i in range(1, n):
            zero_floor[i] += zero_floor[i - 1]
    print(zero_floor[-1])

