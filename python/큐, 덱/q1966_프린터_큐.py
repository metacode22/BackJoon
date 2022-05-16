import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    tmp_q  = deque()
    cnt = 0
    
    for idx, x in enumerate(tmp):
        tmp_q.append((idx, x))
        
    m_value = tmp_q[m][1]
    
    while tmp_q:
        for i in range(1, len(tmp_q)):
            if tmp_q[0][1] < tmp_q[i][1]:
                tmp_q.append(tmp_q.popleft())
                break
        else:
            res = tmp_q.popleft()
            cnt += 1
            if res[1] == m_value and res[0] == m:
                print(cnt)
            