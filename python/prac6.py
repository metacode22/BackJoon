import sys
input = sys.stdin.readline

k = 7
arr = [1, 2, 3, 4, 5, 6, 7]
check_list = [True] * 7
arr_list = []
tmp = [0] * 6

def recur(x):
    if x == 6:
        tmp.sort()
        arr_list.append(tmp.copy())
        return

    else:
        for i in range(len(arr)):
            if check_list[i]:
                tmp[x] = arr[i]
                check_list[i] = False
                recur(x + 1)
                check_list[i] = True

    pass

recur(0)
