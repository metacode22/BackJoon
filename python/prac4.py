import sys
input = sys.stdin.readline

n = int(input())
n_compare = n
cnt = 0
while True:
    # t_1 = t % 10
    # t_10 = t // 10
    # t = t_1 * 10 + t_10

    # if t == n:
    #     break
    # print(t)

    n_10 = n % 10
    n_1 = (n % 10 + n // 10) % 10

    n = n_10 * 10 + n_1

    cnt += 1

    if n == n_compare:
        print(cnt)
        break

