import sys

num_list = []

for i in range(9):
    num = int(sys.stdin.readline())
    num_list.append(num)

max = num_list[0]
count = 0

for j in range(0, len(num_list)):
    if num_list[j] >= max:
        max = num_list[j]

        count = j + 1

print(max)
print(count)

