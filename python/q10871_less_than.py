import sys

n, x = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

for i in num_list:
    if i < x:
        print(i, end=' ')
