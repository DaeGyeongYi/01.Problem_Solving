m = int(input())
n = int(input())
min = 10001
sum = 0

for i in range(m,n+1):
    check = 0
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                check += 1
                break

        if check == 0:
            sum += i
            if i<min:
                min=i0

if min == 10001:
    print(-1)
else:
    print(sum)
    print(min)

