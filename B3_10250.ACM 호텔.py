t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    cnt = 1
    while(n>h):
        n = n-h
        cnt += 1




    print(n*100+cnt)



#씨팔 str타입으로 제출하면 왜 틀리냐고 병신들아이걸로 3시간을 고민했네 병신같은거