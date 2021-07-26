n = int(input())
cnt = 0

for i in range(1,n+1):
    if i <100: #1~99까지는 다 등차수열임
        cnt += 1
    else: # 1000은 그냥 아니니까 100의자리만 신경쓰자
        each = list(map(int, str(i)))
        if each[0]-each[1] == each[1]-each[2]:
            cnt += 1


print(cnt)