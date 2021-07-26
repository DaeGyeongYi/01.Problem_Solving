import sys
n = int(input())
cnt = 0

for _ in range(n):
    string = sys.stdin.readline()
    stack2 = []
    for i in range(len(string)):
        if string[i] not in stack2 or string[i]==string[i-1]:
            stack2.append(string[i])
        else:
            break
    if len(string) == len(stack2):
        cnt +=1

print(cnt)



### 문자열은 배열처럼 취급받는데 왜 스택을 활용했니..?

#공간복잡도에서 좀 더 효율적인 풀이, stack에 append야 어차피 상수시간이잖아요!

# N=int(input())
#
# answer=0
#
# for i in range(N):
#     word = input()
#     for j in range(len(word)):
#         if j!=len(word)-1:
#             if word[j]==word[j+1]:
#                 pass
#             elif word[j] in word[j+1:]:
#                 break
#         else:
#             answer+=1
# print(answer)

