# # 나의 풀이
# t = int(input())
# for _ in range(t):
#     x,y = map(int,input().split())
#     dist = y-x
#     cnt = 1
#
#
#     for i in range(1,int(dist**0.5)+2):
#         if dist> int(i**2):
#             print("i제곱을 지남:",int(i**2))
#             cnt += 1
#             print("이동횟수:",cnt)
#         if dist > int(i**2)-i and i != 1:
#             print("i제곱 -i를 지남:", int(i ** 2) - i)
#             cnt +=1
#             print("이동횟수:",cnt)
#
#     print("최종 이동회수",cnt)

## 직접 하나씩 표로 그려보다보면 이동횟수가 늘어나는 구간이 n제곱을 지날때와, n제곱 -n을 지날때가 있다는 것을 알 수 있다.


#제출용
# 나의 풀이
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    dist = y-x
    cnt = 1


    for i in range(1,int(dist**0.5)+2):
        if dist> int(i**2):
            cnt += 1
        if dist > int(i**2)-i and i != 1:
            cnt +=1

    print(cnt)