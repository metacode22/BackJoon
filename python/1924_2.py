import sys
input = sys.stdin.readline

x, y = map(int, input().split())
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

if x == 1:
    print(day[y % 7])

if x == 2:
    print(day[y % 7 + 3])