s = input().lower()
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_num = [0]*26
cnt = 0

for i in range(len(alpha)):
    for j in range(len(s)):
        if alpha[i] == s[j]:
            alpha_num[i] += 1

for i in alpha_num:
    if i == max(alpha_num):
        cnt +=1


if cnt > 1:
    print("?")
elif cnt == 1:
    print(alpha[alpha_num.index(max(alpha_num))].upper())