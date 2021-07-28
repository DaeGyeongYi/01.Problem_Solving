dials = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

s = input()
cnt =0
for i in s:
    for j in range(len(dials)):
        if i in dials[j]:
            cnt += j+3

print(cnt)
