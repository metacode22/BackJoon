# <DFS>
# def DFS(L):
#     if L == r:
#         print(result)
#     else:
#         for i in range(len(n)):
#             if checklist[i] == 0:
#                 checklist[i] = 1
#                 result[L] = n[i]
#                 DFS(L + 1)
#                 result[L] = 0
#                 checklist[i] = 0
# n = [1, 2 ,3]
# r = 2

# checklist = [0] * r
# result = [0] * r

# DFS(0)

# for 문 이용
# arr = [1, 2, 3]
# r = 3
# for i in range(0, len(arr)):
#     for j in range(0, len(arr)):
#         if i == j:
#             continue
#         for k in range(0, len(arr)):
#             if i == k or j == k:
#                 continue
#             print(i, j, k)

# <for 문 이용 (2)>
# visited = [0] * (3 + 1) # visited[1] = 1이라면 1은 사용중이다, visited[2] = 1이라면 2는 사용중이다라는 뜻.
# arr = [0] * 3
# for i in range(1, 4):
#     visited[i] = 1
#     arr[0] = i
#     for j in range(1, 4):
#         if visited[j]:
#             continue
#         visited[j] = 1
#         arr[1] = j
#         for k in range(1, 4):
#             if visited[k]:
#                 continue
#             visited[k] = 1
#             arr[2] = k
#             print(arr)
#             arr[2] = 0
#             visited[k] = 0
#         arr[1] = 0
#         visited[j] = 0
#     arr[0] = 0
#     visited[i] = 0

# <재귀 이용>
A = [1, 2, 12, 1]           # 데이터 집합
N = len(A)              # 데이터 갯수
visited = [0] * N       # 데이터 사용 여부. visited[1] = 1은 1번을 사용했다는 뜻.
arr = [0] * N           # 어떤 데이터를 선택했는가(순열 정보 저장) arr[1] = 2라면 두번째(arr[1]의 1)로 뽑은 숫자는 2다.
arr_list = []
def permutation(level):
    if level >= N:      # level이 0부터 시작한다고 치면,
                        # 0에서 1개를 선택하고, 1에서 1개를 선택하고, 2에서 1개를 선택하면
                        # 총 3개를 뽑았으니 더 이상 카드를 뽑을 필요가 없다.
                        # 따라서 level이 3이 되어 level >= N이라는 if문을 만나 return으로 종료된다.
        arr_list.append(arr.copy())
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1  # i번째 index는 사용 중이다.
        arr[level] = A[i]
        permutation(level + 1)
        arr[level] = 0
        visited[i] = 0

permutation(0)
print(arr_list)



