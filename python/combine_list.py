# a와 b는 이미 오름차순으로 정렬된 리스트들이다.
# 이미 오름차순으로 정렬되어 있을 때 sort를 쓰는 것은 비효율적. sort의 Big O는 N*logN
# 이미 오름차순으로 정렬되어 있을 때 밑의 코드를 사용하면 Big O는 N이 된다.
n = 3
a = [1, 3, 5]
m = 5
b = [2, 3, 6, 7, 9]
tmp = []
p1 = 0
p2 = 0

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        tmp.append(a[p1])
        p1 += 1
    else:
        tmp.append(b[p2])
        p2 += 1

# while이 끝나고 p1이 n보다 작으면,
# 즉 p2가 가르킬 수 있는 갯수인 m이 p1의 n보다 적기 때문에 p2로 인해 while이 먼저 끝났기 때문이다.
# p1은 아직 n에 닿지 못했다는 뜻이다.

if p1 < n:
    tmp = tmp + a[p1:] # p1이 가르키고 있는 값은 아직 못들어간 상태일 것이다.

if p2 < m:
    tmp = tmp + b[p2:]

print(tmp)


