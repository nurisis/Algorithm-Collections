"""
p. 217

연산 4개를 사용해 1을 만드려고 한다.
최소 횟수

** 점화식
>> F(i) = min(F(i-1), F(i//2), F(i//3), F(i//5)) + 1
"""

x = int(input())

# 계산 결과를 담는 DP 테이블
d = [0] * 30001

for i in range(2, x+1):
    # 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 3로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
