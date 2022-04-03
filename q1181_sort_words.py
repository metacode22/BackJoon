import sys

n = int(sys.stdin.readline())
arr = []
set_arr = []

for _ in range(n):
    str = sys.stdin.readline().rstrip()
    arr.append(str)

set_arr = set(arr)
arr = list(set_arr)

                                            # print('--')
                                            # print('set_arr', set_arr)
                                            # print('arr', set_arr)
arr.sort()
                                            # print('sorted arr', arr)
arr.sort(key = len)
                                            # print('sorted arr by len', arr)

for i in arr:
    print(i)