n= int(input())
cnt = 0
n_list=[]
if n <10:
    n_list.append(0)
    n_list.append(n)
else:
    n_list= list(map(int, str(n)))




while True:
    new = n_list[1]*10 + ((n_list[0]+n_list[1])%10)
    if new < 10:
        n_list = list(map(int, str(new)))
        n_list.insert(0,0)
    else:
        n_list = list(map(int, str(new)))
    cnt+=1
    if new == n:
        print(cnt)
        break

