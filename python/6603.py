import sys
input = sys.stdin.readline

k = 7
arr = [1, 2, 3, 4, 5, 6, 7]
arr_list = set()
check_list = [True] * k

tmp = [0] * 6

for i in range(6):
    tmp.append(arr[i])

def recur(x):
    if x == 6:
        tmp.sort()
        print(tmp)
        # arr_list.add(tmp.copy())
        return

    else:
        for i in range(len(arr)):
            if check_list[i]:
                tmp[x] = arr[i]
                check_list[i] = False
                recur(x + 1)
                check_list[i] = True

recur(0)

# 미해결

