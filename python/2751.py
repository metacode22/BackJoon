import sys

t = int(sys.stdin.readline())
arr = []

for _ in range(t):
    n = int(sys.stdin.readline())
    arr.append(n)

def merge_sort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2

        merge_sort(lt, mid)
        merge_sort(mid + 1, rt)

        p1 = lt
        p2 = mid + 1
        tmp = []

        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1

        if p1 <= mid:
            tmp = tmp + arr[p1:(mid + 1)]
        if p2 <= rt:
            tmp = tmp + arr[p2:(rt + 1)]


        for i in range(len(tmp)):
            arr[lt + i] = tmp[i]

merge_sort(0, t - 1)

for j in arr:
    print(j)