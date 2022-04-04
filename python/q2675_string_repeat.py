import sys

t = int(sys.stdin.readline())

for i in range(t):
    input_list = sys.stdin.readline().split()
    n = int(input_list[0])
    string = input_list[1]
    sum = ''
    for j in range(len(input_list[1])):
        sum += string[j]*n
    print(sum)