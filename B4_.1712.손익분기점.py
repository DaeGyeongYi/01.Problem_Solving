fixed_cost, variable_cost, price = map(int, input().split())



surplus=price-variable_cost
if surplus<=0:
    print(-1)
else:
    print(fixed_cost//surplus+1)


#재귀함수나 반복문 썼다가는 큰 케이스 대입되었을때 난감해집니당