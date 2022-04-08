import sys

input = sys.stdin.readline

import math
a, b, v = map(int, input().split())
print(math.ceil((v-b) / (a-b)))

# 달팽이는 하루에 총 a-b만큼 간다.
# 마지막 날에는 올라가기만 한다. 즉 마지막 날에는 +a만 한다는 것.
# 마지막 날 내려가는 b는 필요 없으므로 v-b가 총 길이다.