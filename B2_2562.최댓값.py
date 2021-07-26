import sys

n_list = []

for _ in range(9):
    num = int(sys.stdin.readline())
    n_list.append(num)

for i in range(len(n_list)):
    if max(n_list) == n_list[i]:
        print("%d\n%d"%(max(n_list),i+1))