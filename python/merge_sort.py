# 리스트를 실제로 자르는 것이 아니라 포인터가 lt와 rt의 시작을 가르키게 하는 방식이다.
# 따라서 extend를 써서 합치거나 배열을 실제로 자르는 등의 코드는 필요치 않다.
arr = [23, 11, 45, 36, 15, 67, 33, 21]

def merge_sort(lt, rt):
    if lt < rt:                         # lt가 왼쪽에 있으니 수가 더 적다. 그리고 lt와 rt가 같아진다는 것은 값을 1개 가지고 있다는 뜻이다.
        mid = (lt + rt) // 2            # 여기서는 D(0, 7)이므로 mid는 3이다.
        merge_sort(lt, mid)
        merge_sort(mid + 1, rt)

# 이렇게 Dsort로 재귀되는 일들을 다 끝내고 오면 본연의 일을 해야 한다.
# 여기서 p는 pointer(포인터)
        p1 = lt
        p2 = mid + 1
        tmp = []

# p1의 끝은 mid이고, p2의 끝은 rt이다. 어느 하나라도 끝에 닿으면 while이 끝나게 한다.
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1                 # lt에서 p1이 가르키는 값은 더 이상 비교가 필요 없으니 오른쪽으로 이동한다.
            else:
                tmp.append(arr[p2])
                p2 += 1                 # rt에서 p2가 가르키는 값은 더 이상 비교가 필요 없으니 오른쪽으로 이동한다.

        if p1 <= mid:               # p1이 mid보다 작거나 같으면 p1이 가르키고 있는 값들이 아직 tmp에 못들어간 상황이다.
            tmp = tmp + arr[p1:(mid+1)]     # mid까지. 만약 mid가 3이라면 해당 식은 2까지만 간주한다.
        if p2 <= rt:
            tmp = tmp + arr[p2:(rt+1)]

# for문으로 넣을 때 그냥 arr[i] = tmp[i] 해버리면
# 예로 merge_sort(4, 7)dl 실행되었을 때, i는 0부터 시작하므로
# arr[0] = tmp[0], arr[1] = tmp[1]...이 된다.
        for i in range(len(tmp)):
            arr[lt + i] = tmp[i]



print('Before sort : ', end='')
print(arr)
merge_sort(0, 7)
print()
print('After sort : ', end='')
print(arr)