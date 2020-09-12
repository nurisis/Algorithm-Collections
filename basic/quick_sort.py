"""
평균 : O(NlogN)
최악 : O(N2)
"""


def quick_sort(arr, start, end):
    # 배열의 크기가 1이면, 정렬이 완료되었다고 본다
    if start >= end:
        return

    # pivot은 첫번째 원소
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # left 는 pivot보다 큰값을 찾을때까지 오른쪽으로 이동
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # right 는 pivot보다 작은값을 찾을때까지 쪽으로 이동
        while right > start and arr[pivot] <= arr[right]:
            right -= 1

        # left와 right이 엇갈렸을 경
        if left > right:
            # pivot과 right이 가리키는 수 스위치
            arr[pivot], arr[right] = arr[right], arr[pivot]
            pivot = right
        # left 와 right 스위치
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # pivot 기준 왼쪽 다시 퀵정렬
    quick_sort(arr, start, pivot-1)
    # pivot 기준 오른쪽 다시 퀵정렬
    quick_sort(arr, pivot + 1, end)


# arr = [7, 6, 5, 4, 3, 2, 1]
# arr = [10, 100, 3, 9, 4, 2, 88, 66, 23, 41, 23]
arr = [10, 100, 3, 9, 4, 2, 88, 66, 23, 41, 1000, 322, 678, 2, 1, 412]
quick_sort(arr, 0, len(arr) - 1)
print(arr)