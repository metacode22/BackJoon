import sys

t = int(sys.stdin.readline())

for i in range(t):
    ox = list(sys.stdin.readline().rstrip())
    sum = 0
    count = 0
    for j in ox:
        if j == 'O':
            count += 1
            sum += count
        else:
            count = 0

    print(sum)
