from sys import stdin

def cal():
    n = int(stdin.readline())
    sum = 0
    for j in range(n):
        each = int(stdin.readline())
        sum += each
    if sum > 0:
        print('+')
    elif sum == 0:
        print(0)
    else:
        print('-')



cal()
cal()
cal()

## stdin.readline()을 안쓰면 시간초과가 계속 난다.
## 중첩 for문이 문제인줄 알고 함수로 바꿔서 for문하나 줄이기까지했는데..
## 사실 그게 의미가 없음을 알지만 그냥 해봤다..for문 줄어들면 시간복잡도 줄거라는 막연한 희망으로