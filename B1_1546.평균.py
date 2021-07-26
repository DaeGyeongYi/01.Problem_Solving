import sys

n = int(input())
score = []
new = []

score = list(map(int,sys.stdin.readline().split()))


for i in range(n):
    new.append(score[i]/max(score))

print((sum(new)/n)*100)