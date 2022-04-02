import sys

c = int(sys.stdin.readline())

for i in range(c):
    input_list = list(map(int, sys.stdin.readline().split()))
    n = input_list[0]
    del input_list[0]
    ave = sum(input_list)/n
    count = 0
    for j in input_list:
        if j > ave:
            count += 1
    print('{:.3f}%'.format((count/n)*100))
