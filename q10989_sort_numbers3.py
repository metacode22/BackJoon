# 계수 정렬, Counting Sort

from array import array
import sys

t = int(sys.stdin.readline())

# 문제에서 입력값으로 주어질 수 있는 N은 10000 이하의 자연수이다.
# (0도 그냥 추가) 따라서 0 부터 10000까지, N이 입력될 때마다 갯수를 셀 수 있는 배열(count_arr)을 생성한다.
count_arr = [0 for _ in range(10001)]
arr = []

for i in range(t):
    n = int(sys.stdin.readline())

# count_arr는 0부터 시작하므로 count_arr[0] = 0 이다.
# 따라서 index와 그 index에 해당하는 값(여기서는 n)이 처음에는 일치한다.
# n이 입력되면 n에 해당하는 count_arr의 값을 count한다.(1을 더한다)
    count_arr[n] += 1

# 0 ~ 10000까지의 배열인 count_arr를 모두 순회하면서 해당 값이 0이 아니면 값을 출력해야 한다.
# 해당 값이 만약 2라면, 앞 단계에서 n이 2번 입력되어 2번 count된 것이므로 2번 출력해줘야 한다.
# 즉 count_arr의 index를 n만큼 출력해줘야 한다.
for j in range(10001):
    if count_arr[j] != 0:
        for k in range(count_arr[j]):
            print(j)