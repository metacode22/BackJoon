import sys
input = sys.stdin.readline

t = int(input())
arr = []

for _ in range(t):
    n = int(input())
    arr.append(n)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for k in arr:
    print(k)