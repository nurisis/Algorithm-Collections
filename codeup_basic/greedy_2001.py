# 파파 파스타 가게는 점심 추천 파스타와 생과일 쥬스 세트 메뉴가 인기가 좋다.
#
# 이 세트 메뉴를 주문하면 그 날의 3 종류의 파스타와 2 종류의 생과일 쥬스에서 하나씩 선택한다.
#
# 파스타와 생과일 쥬스의 가격 합계에서 10%를 더한 금액이 대금된다.
#
# 어느 날의 파스타와 생과일 쥬스의 가격이 주어 졌을 때, 그 날 세트 메뉴의 대금의 최소값을 구하는 프로그램을 작성하라.

pasta1 = int(input(''))
pasta2 = int(input(''))
pasta3 = int(input(''))

juice1 = int(input(''))
juice2 = int(input(''))

min_pasta_price = min(pasta1, pasta2, pasta3)
min_juice_price = min(juice1, juice2)

min_price = (min_juice_price+min_pasta_price)*1.1

print(round(min_price, 1))
