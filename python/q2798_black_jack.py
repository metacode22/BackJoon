import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum_list = []

res = 0
for i in range(0, n):
    sum = 0
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = arr[i] + arr[j] + arr[k]

            if sum <= m:
                res = max(res, sum)

print(res)



# itertools 라이브러리를 이용한 방법
import sys
from itertools import permutations                  # permutation, 순열

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
permutationArr = permutations(arr, 3)

res = 0
for i in permutationArr:
    if sum(i) <= m:
        res = max(res, sum(i))

print(res)