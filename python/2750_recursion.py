import sys
input = sys.stdin.readline

t = int(input())
arr_input = []

for _ in range(t):
    n = int(input())
    arr_input.append(n)

arr_origin = arr_input.copy()

def recur(arr, x):
    if x == len(arr) - 1:
        return

    else:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                recur(arr, i + 1)

recur(arr_input, 0)

print('origin', arr_origin)
print('changed', arr_input)

for j in arr_input:
    print(j)