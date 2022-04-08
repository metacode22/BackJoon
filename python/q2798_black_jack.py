import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_list = []

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                sum_list.append(arr[i] + arr[j] + arr[k])

print(max(sum_list))

# itertools 라이브러리를 이용한 방법
# import sys
# from itertools import permutations                  # permutation, 순열

# n, m = map(int, sys.stdin.readline().split())

# arr = list(map(int, sys.stdin.readline().split()))
# permutationArr = permutations(arr, 3)

# res = 0
# for i in permutationArr:
#     if sum(i) <= m:
#         res = max(res, sum(i))

# print(res)