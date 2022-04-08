import sys
input = sys.stdin.readline

arr = []

for _ in range(9):
    n = int(input())
    arr.append(n)

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            num1 = arr[i]
            num2 = arr[j]

            arr.remove(num1)
            arr.remove(num2)
            break

    if len(arr) == 7:
        break

for k in range(len(arr)):
    for l in range(k + 1, len(arr)):
        if arr[k] > arr[l]:
            arr[k], arr[l] = arr[l], arr[k]

for k in arr:
    print(k)