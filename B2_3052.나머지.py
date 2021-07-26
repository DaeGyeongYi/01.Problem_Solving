import sys

n_list=[]

for _ in range(10):
    a = int(sys.stdin.readline())
    n_list.append(a%42)


print(len(list(set(n_list))))