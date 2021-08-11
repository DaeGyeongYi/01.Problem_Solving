def sugar(n):
    min = 5000
    for i in range(n // 5 + 1):
        for j in range(n // 3 + 1):
            sum = i * 5 + j * 3
            each = i+j
            if sum == n:
                if min > each:
                    min = i+j
    if min == 5000:
        return -1
    else:
        return min



n = int(input())



print(sugar(n))
