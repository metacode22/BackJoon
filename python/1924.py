import sys
input = sys.stdin.readline

date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

x, y = map(int, input().split())
n = 0

for i in range(0, x - 1):
    n += date[i]

print(day[(n + y) % 7])