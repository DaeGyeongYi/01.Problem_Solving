import sys
n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))


print(min(n_list), max(n_list))


