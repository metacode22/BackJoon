# 유망하다면 계속 판다.
# 유망하지 않다면 자식 노드들을 계속 체크한다.
# 해답을 못 만나면 부모 노드로 간다.

# 임의의 집합(set): 체스 보드에 있는 n^2개의 가능한 위치.
# 기준(criterion): 새로 놓을 퀸이 다른 퀸을 위협할 수 없음. 위협할 자리를 배제한다.
# 원소의 순서(sequence): 퀸을 놓을 수 있는 n개의 위치.
# 가지치기(prune)를 어떻게 할 것인가, 이는 반대로 어떤 것이 유망한가(promising)와 같다.

import sys

n = int(sys.stdin.readline())

cnt = 0

def promising(i):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag

def n_queens(i):

    global cnt

    n = len(col) - 1
    if (promising(i)):
        if (i == n):
            # print(col[1: n + 1])
            cnt += 1
            return

        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i + 1)

col = [0] * (n + 1)
n_queens(0)
print(cnt)
