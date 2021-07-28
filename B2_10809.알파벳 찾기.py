alpha_num = [-1]*26
alpha = 'abcdefghijklmnopqrstuvwxyz'


str = input()

for i in range(len(alpha)):
    for j in range(len(str)):
        if alpha[i] == str[j] and alpha_num[i] == -1:
            alpha_num[i] = j

for i in alpha_num:
    print(i,end=' ')
