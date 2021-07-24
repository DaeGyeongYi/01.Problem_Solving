import sys
#
# def n_sum():
#     a=[]
#     n = int(input())
#
#     for _ in range(n):
#         k = int(sys.stdin.readline())
#         a.append(k)
#     return sum(a)
#
#
# print(n_sum())

# 이렇게 해도 풀리지만 백준에서 주어진 형식대로는 이렇게

def solve(a):
    ans = 0

    for i in a:
        ans += i
    return ans

n = int(input())
a = [int(sys.stdin.readline()) for _ in range(n)]

print(solve(a))


## 제출은 함수만 해도 되는듯
# 리스트까지 만든 성실한 나 칭찬해!