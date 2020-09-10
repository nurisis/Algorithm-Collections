"""
큰 수를 표현할 때 자릿수를 쉽게 구분하기 위해 천단위 구분 기호인 콤마(,)를 사용한다.
어떤 수가 입력되면 천단위 구분 기호를 넣어 그 수를 다시 출력하는 프로그램을 작성하시오.

첫째 줄에 숫자의 길이 n이 입력된다. (1≤n≤200)
둘째 줄에 길이가 n인 숫자가 입력된다.
"""

# 내 풀이 2 => 25 ms
# n = int(input())
# number = input()
#
# stack = []
# new_num = ''
#
# check = 0
# for i in range(1, n+1):
#     if i == n:
#         new_num = number[0] + new_num
#     else:
#         check += 1
#         new_num = number[-i] + new_num
#         if check == 3:
#             new_num = ',' + new_num
#             check = 0
# print(new_num)

# 내 풀이 1 => 20 ms
n = int(input())
number = input()

stack = []
new_num = ''
for i in number:
    stack.append(i)

check = 0
while stack:
    check += 1
    new_num = stack.pop() + new_num
    if check == 3 and stack:
        new_num = ',' + new_num
        check = 0

print(new_num)
