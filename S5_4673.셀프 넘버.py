def d(num_list):
    for i in range(1,10000): #1~10000까지 셀프넘버를 체크하기 위한 식
        k = 0
        for j in str(i):
            k += int(j)
        if k+i in num_list:
            num_list.remove(k+i)
    return num_list



num_list = [i for i in range(1,10000)]# 10000까지의 숫자가 담긴 리스트

for i in d(num_list):
    print(i)
