inputList = [10, 20, 25, 35, 45, 55, 60, 75, 85, 90]
length = len(inputList)

# 재귀 방식의 이진 탐색
def binarySearch(arr, left, right, k):  # 순서대로 받는 리스트, 좌측값, 우측값, 찾아야하는 숫자 K
    # 1 중간 값 찾기
    mid = (left + right) // 2
    print(mid)

    # 2 중간값이 K와 같을때
    if k == arr[mid]:
        print(f"Value = {arr[mid]} ")
        return True

    # 값이 다를 떄 (중간값이 k 보다 클 때
    elif arr[mid] > k:
        return binarySearch(arr, left, mid - 1, k) #재귀 호출
    elif arr[mid] < k:
        return binarySearch(arr, mid + 1, right, k) # 재귀 호출
    else:
        return False


print("55: ", binarySearch(inputList, 0, length - 1, 55))
