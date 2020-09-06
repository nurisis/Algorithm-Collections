a, b = input('').split()

degree = abs(int(a) - int(b))

remainder_10 = degree % 10
if remainder_10 > 7:
    by_10 = degree // 10 + 1
    by_5 = 0
    by_1 = abs(degree - by_10 * 10)
elif 5 > remainder_10 > 3:
    by_10 = degree // 10
    by_5 = (degree % 10) // 5 + 1
    by_1 = abs(degree % 10 - by_5 * 5)
else:
    by_10 = degree // 10  # 1
    by_5 = (degree % 10) // 5  # 1
    by_1 = (degree % 5)

print(by_10 + by_5 + by_1)
