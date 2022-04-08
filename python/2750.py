import sys

t = int(sys.stdin.readline())

num_list = []

# 버블 정렬
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     num_list.append(n)

# for i in range(len(num_list)):
#     for j in range(len(num_list)):
#         if num_list[i] < num_list[j]:
#             num_list[i], num_list[j] = num_list[j], num_list[i]

# 삽입 정렬
# num_list = [8, 3, 2, 7, 6]

# for i in range(1, len(num_list)):
#     for j in range(i, 0, -1):
#         if num_list[j - 1] > num_list[j]:
#             num_list[j], num_list[j - 1] = num_list[j - 1], num_list[j]

# 삽입 정렬 최적화
# for i in range(1, len(num_list)):
#     j = i

#     while j > 0 and num_list[j - 1] > num_list[j]:
#         num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]
#         j -= 1

for i in num_list:
    print(i)

