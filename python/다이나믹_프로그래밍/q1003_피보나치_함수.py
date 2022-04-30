# <나의 풀이 - 1> : 시간 초과 발생
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# def DFS(x):
#     global cnt0, cnt1
    
#     if x == 0:
#         cnt0 += 1
#         return 0
    
#     if x == 1:
#         cnt1 += 1
#         return 1
        
#     else:
#         return DFS(x - 1) + DFS(x - 2)

# t = int(input())
# for _ in range(t):
#     cnt0 = 0
#     cnt1 = 0
#     n = int(input())
#     DFS(n)
#     print(cnt0, cnt1)
    


# <나의 풀이 - 2> : DP 테이블 2개 생성, 성공
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 0:
        print(1, 0)
        
    else:
        dp_0 = [0] * (n + 1)
        dp_1 = [0] * (n + 1)
        dp_0[0] = 1
        dp_0[1] = 0
        dp_1[0] = 0
        dp_1[1] = 1
        
        for i in range(2, n + 1):
            dp_0[i] = dp_0[i - 1] + dp_0[i - 2]
            dp_1[i] = dp_1[i - 1] + dp_1[i - 2]
        
        print(dp_0[-1], dp_1[-1])
        