n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    a %= 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    else:
        b %= 4
        if b == 0:
            b=4
        print(a**b%10)

# 냅다 반복문에 a**b%10 하면 케이스가 커질때 곤란쓰
# 어차피 a는 1의자리수만 고민하면 되니까 %10연산을 통해 크기를 줄이고
#b는 특정케이스들은 거르고, 나머지 케이스는는 4개단위로 반복이 형성됨
#b에도 나머지연산을 통해 몫만큼 사이클을 돌고 마지막 사이클에서 도착할 값을 알수 있다.
#4번째에 위치하는 경우는 %연산으로는 0이 나와버리니까
#if문으로 b=4로 고쳐줌
