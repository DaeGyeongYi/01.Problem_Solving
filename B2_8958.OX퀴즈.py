import sys

n = int(input())

for _ in range(n):
    OX = list(sys.stdin.readline().rstrip())
    score = 0
    cnt = 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            cnt +=1
            score += cnt
        else:
            cnt = 0
    print(score)