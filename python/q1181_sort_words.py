import sys
input = sys.stdin.readline

n = int(input())
str_set = set()

for _ in range(n):
    str = input().rstrip()
    str_set.add(str)

str_list = list(str_set)
str_list.sort()             # 알파벳 순으로 정렬
str_list.sort(key = len)    # 길이 순으로 정렬
                            # 길이로 순으로 먼저 정렬하면 알파벳 순이 꼬인다.
for i in str_list:
    print(i)