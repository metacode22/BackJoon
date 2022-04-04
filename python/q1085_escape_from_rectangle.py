import sys

x, y, w, h = map(int, sys.stdin.readline().split())
distance_list = []

x_w = abs(x - w)
x_0 = abs(x)
y_h = abs(y - h)
y_0 = abs(y)

distance_list.append(x_w)
distance_list.append(x_0)
distance_list.append(y_h)
distance_list.append(y_0)

print(min(distance_list))