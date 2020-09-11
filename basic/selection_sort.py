"""
시간복잡도 O(N2)
"""

arr = [7, 6, 5, 4, 3, 2, 1]

arr_len = len(arr)
for i in range(arr_len):
    min_idx = i
    for j in range(i+1, arr_len):
        # 가장 작은수를 찾는다
        if arr[j] < arr[min_idx]:
            min_idx = j

    # 가장 작은수와 현재 수와 교환
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)