import sys

n = int(input())
cnt_n = 0
num = sys.stdin.readline().split()

for i in range(len(num)):
    cnt = 0

    for j in range(1,int(num[i])+1):
        if int(num[i])%j == 0:
            cnt += 1
    if cnt==2:
        cnt_n += 1

print(cnt_n)



## 굉장히 지저분한 코드이므로 다른 것 찾아봄
# num_count = int(input())
# num_list = list(map(int, input().split(' ')))
# res = 0
#
# if len(num_list) == num_count:  # 첫 입력 수와 리스트의 갯수가 일치할때만 작동
#     for i in num_list:  # 리스트를 순차적으로 순환
#         count = 0  # 소수는 1과 자기자신으로만 나뉘는수 (수를 세기위한 count)
#         for j in range(1, i + 1):  # 1부터 리스트의 수까지 진행
#             if i % j == 0:  # i가 j로 나누어 진다면
#                 count += 1  # 나뉘는수 +1 증가
#         if count == 2:  # 나뉘는수가 2개다 = 소수
#             res += 1  # 리스트의 i항은 소수이다.
# print(res)

##에라토스테네스의 체 알아볼것