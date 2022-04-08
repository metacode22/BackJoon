import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
x_list = [0, w]
y_list = [0, h]

x_length = []
y_length = []

for _ in range(n):
    axis, num = map(int, input().split())

    if axis == 0:
        y_list.append(num)

    if axis == 1:
        x_list.append(num)

x_list.sort()
y_list.sort()

for i in range(len(x_list) - 1):
    x_length.append(x_list[i + 1] - x_list[i])

for j in range(len(y_list) - 1):
    y_length.append(y_list[j + 1] - y_list[j])

print(max(x_length) * max(y_length))