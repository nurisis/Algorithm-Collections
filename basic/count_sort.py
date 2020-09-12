"""
계수 정렬.
데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 매우 빠름.

O(N + K)
* K = 데이터 중 최대값
"""


def count_sort(array):
    count = [0] * (max(array)+1)

    for i in array:
        count[i] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')

    # # 내 풀이
    # max_value = max(array)
    # min_value = min(array)
    # temp_arr = [0] * (max_value-min_value+1)
    #
    # for i in array:
    #     temp_arr[i-min_value] += 1
    #
    # result = ''
    # for i in range(len(temp_arr)):
    #     num = temp_arr[i]
    #     if num != 0:
    #         result += (str(i+min_value) + " ") * num
    #
    # return result


n = int(input())
arr = list(map(int, input().split()))
count_sort(arr)