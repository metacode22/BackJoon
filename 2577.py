import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

mul = A*B*C
str_list = list(str(mul))

for i in range(10):
    str_num = str(i)
    count = str_list.count(str_num)
    print(count)