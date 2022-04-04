import sys

arr = [int(sys.stdin.readline()) for _ in range(9)]

tot = sum(arr)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if tot - (arr[i] + arr[j]) == 100:
# arr를 참조
            # arr.remove(arr[i])
            # arr.remove(arr[j - 1])

# 변수로 값을 찾아 제거. remove() 안에서 arr를 따로 참조하지 않음.
            num1, num2 = arr[i], arr[j]
            arr.remove(num1)
            arr.remove(num2)

            arr.sort()
            break

    if len(arr) < 9:
        break

for k in arr:
    print(k)

# for문 모두 탈출이 필요