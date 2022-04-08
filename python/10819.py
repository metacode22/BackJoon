import sys
from itertools import permutations
input = sys.stdin.readline

n = map(int, input().split())
arr = list(map(int, input().split()))

permutationArr = permutations(arr)

res = -2147000000
for i in permutationArr:
    sum = 0
    for j in range(len(i) - 1):
        sum += abs(i[j] - i[j + 1])

    if res <= sum:
        res = sum

print(res)

# 순열(permutation)을 재귀로 직접 생성

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# visited = [False] * n
# tmp = [0] * n
# arr_list = []

# def permutation(level):
#     if level >= n:

#         arr_list.append(tmp.copy())

#     for i in range(n):
#         if visited[i]:
#             continue
#         visited[i] = True
#         tmp[level] = arr[i]
#         permutation(level + 1)
#         tmp[level] = 0
#         visited[i] = False

# permutation(0)

# res = -2147000000
# for i in arr_list:
#     sum = 0
#     for j in range(len(i) - 1):
#         sum += abs(i[j] - i[j + 1])
#     if sum > res:
#         res = sum

# print(res)

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr_input = list(map(int, input().split()))
# arrs = []
# check_list = [True] * n
# tmp = [0] * n
# sum_list = []

# def permutation(arr, x):
#     if x == n:
#         arrs.append(tmp.copy())
#         return

#     else:
#         for i in range(0, len(arr)):
#             if check_list[i]:
#                 tmp[x] = arr[i]
#                 check_list[i] = False
#                 permutation(arr, x + 1)
#                 check_list[i] = True

# permutation(arr_input, 0)

# # res = -2147000000
# # for j in arrs:
# #     tot = 0
# #     for k in range(0, len(j) - 1):
# #         for l in range(k + 1, k + 2):
# #             tot += abs(j[k] - j[l])
# #         # if k == (len(j) - 1):
# #         #     break
# #     if tot > res:
# #         res = tot

# # print(res)

# res = -2147000000
# for j in arrs:
#     tot = 0
#     for k in range(0, len(j) - 1):
#         tot += abs(j[k] - j[k + 1])
#     if tot > res:
#         res = tot

# print(res)
