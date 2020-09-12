"""
평균 : O(NlogN)
최악 : O(N2)
"""


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    # pivot보다 작은 값의 리스트
    left_side = [x for x in tail if x <= pivot]
    # pivot보다 큰 값의 리스트
    right_side = [y for y in tail if y > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


arr = [10, 100, 3, 9, 4, 2, 88, 66, 23, 41, 1000, 322, 678, 2, 1, 412]
print(quick_sort(arr))