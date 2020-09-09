"""
p. 220

** 점화식
=> F(x) = max(F(x-1), F(X-2) + array[x])
"""
# 책 답안
n = int(input())
food_list = list(map(int, input().split()))

d = [0] * 100

d[0] = food_list[0]
d[1] = max(food_list[0], food_list[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + food_list[i])

print(d[n-1])

# 내 답안
# n = int(input())
# food_list = input().split()
#
# d = [0] * n
# d[0] = int(food_list[0])
# d[1] = int(food_list[1])
#
# for i in range(2, n):
#     if i == 2:
#         d[i] = max(d[i-2] + int(food_list[i]), d[i-1])
#         print(f"[{i}] d[{i}]={d[i]}")
#     else:
#         d1 = d[i-2] + int(food_list[i])
#         d2 = d[i-3] + int(food_list[i-1])
#
#         d[i] = max(d1, d2)
#         print(f"[{i}] d1:{d1}, d2:{d2}, d[{i}]={d[i]}")
#
# print(d[n-1])

