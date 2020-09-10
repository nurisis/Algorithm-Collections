"""
큰 수 덧셈에 성공했다.
이번에는 큰 수 뺄셈에 도전하자.

큰 수 a, b가 두 줄에 걸쳐 입력된다. (a, b는 100자리 이하)
a-b의 결과를 출력한다.
"""

a = input()
b = input()

stack_a = [i for i in a]
stack_b = [i for i in b]

max_n = len(a)
# if b > a:
#     max_n = len(b)

for i in range(1, max_n+1):
    minus = a[-i] - b[-i]
    if minus < 0:
        next = a[-i-1]