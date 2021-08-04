n = int(input())
start = 1
cnt = 1
plus = 6
if n == 1:
    print(cnt)
while n > 1:
    start += plus*cnt
    cnt += 1
    if n<=start:
        print(cnt)
        break



##문제좀 똑바로 읽자..