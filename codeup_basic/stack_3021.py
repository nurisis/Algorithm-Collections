"""
int는 32비트, long long 은 64비트라서 이 보다 더 큰 숫자는 저장할 수 없다.
아주 큰 숫자의 덧셈을 하려고 한다.
계산 결과를 출력하시오.

첫째줄과 둘째줄에 큰 수 a, b가 입력된다. (a, b는 100자리 이하의 정수)

예시.
12345678910111213
2839287
"""
# 내 풀이 2 => 23ms
# a = input()
# b = input()
# stack_a = [i for i in a]
# stack_b = [i for i in b]
#
# stack_sum = []
#
# extra = 0
# while stack_a or stack_b:
#     if stack_a:
#         n1 = int(stack_a.pop())
#     else:
#         n1 = 0
#     if stack_b:
#         n2 = int(stack_b.pop())
#     else:
#         n2 = 0
#
#     s = n1 + n2 + extra
#     extra = s // 10
#     stack_sum.append(s % 10)
#
# if extra > 0:
#     stack_sum.append(extra)
# result = ''
# while stack_sum:
#     result += str(stack_sum.pop())
# print(result)

# 내 풀이 1 => 22
a = input()
b = input()

stack_a = [i for i in a]
stack_b = [i for i in b]

stack_sum = []
number = 0
while stack_a or stack_b:
    if stack_a:
        n1 = int(stack_a.pop())
    else:
        n1 = 0
    if stack_b:
        n2 = int(stack_b.pop())
    else:
        n2 = 0

    n = n1 + n2 + number
    if n >= 10:
        stack_sum.append(n % 10)
        number = n // 10
    else:
        stack_sum.append(n)
        number = 0

if number > 0:
    stack_sum.append(number)
result = ''
while stack_sum:
    result += str(stack_sum.pop())

print(result)