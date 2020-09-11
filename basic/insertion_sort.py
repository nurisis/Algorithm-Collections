"""
시간복잡도 O(N2)
단, 현재 리스트가 거의 정렬되어 있는 상태라면 매우 빠름.
최선의 경우 O(N)
"""

arr = [10, 1, 4, 9, 6, 8, 3, 2]
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]

length = len(arr)
# 삽입정렬에서는, 첫번째 숫자는 정렬이 되어있다고 가정
for i in range(1, length):
    for j in range(i, 0, -1):
        # 현재 숫자가 앞의 숫자보다 작으면 스위치
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        # 현재보다 작은 숫자를 만나면 멈춤
        else:
            break

# # 내 풀이
# length = len(arr)
# for i in range(1, length):
#     num = arr[i]
#     for j in range(i):
#         if num < arr[j]:
#             arr = [arr[n] for n in range(len(arr)) if n != i]
#             arr.insert(j, num)
#             break

print(arr)