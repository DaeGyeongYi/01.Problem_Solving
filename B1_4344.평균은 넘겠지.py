import sys

c = int(input())


for _ in range(c):
    score = list(map(int,sys.stdin.readline().split()))
    cnt = 0
    del score[0]
    mean = sum(score)/len(score)
    for i in range(len(score)):
        if score[i] > mean:
            cnt += 1
    print("%.3f%%"%((cnt/len(score))*100))


