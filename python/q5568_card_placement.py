# import sys
# input = sys.stdin.readline

# from itertools import permutations

# arr = []
# n, k = int(input()), int(input())

# for _ in range(n):
#     arr.append(int(input()))

# res = set()

# for i in list(permutations(arr, k)):
#     res.add(''.join(list(map(str, i))))

# print(res)
# print(len(res))

import sys
input = sys.stdin.readline

t = int(input())
k = int(input())
arr_input = []
check_list = [True] * t
arrs = []
arrs_set = set()
tmp = [0] * k

for _ in range(t):
    n = int(input())
    arr_input.append(n)

def permutation(x):
    global k

    if x == k:
        arrs.append(tmp.copy())
        return

    else:
        for i in range(t):
            if check_list[i]:
                tmp[x] = arr_input[i]
                check_list[i] = False
                permutation(x + 1)
                check_list[i] = True

permutation(0)

for j in arrs:
    arr_joined = ''.join(list(map(str, j)))
    arrs_set.add(arr_joined)

print(len(arrs_set))
