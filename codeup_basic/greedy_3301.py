money = int(input())

remainder_50000 = money//50000
remainder_10000 = (money%50000)//10000
remainder_5000 = (money%10000)//5000
remainder_1000 = (money%5000)//1000
remainder_500 = (money%1000)//500
remainder_100 = (money%500)//100
remainder_50 = (money%100)//50
remainder_10 = (money%50)//10

print(remainder_50000+remainder_10000+remainder_5000+remainder_1000+remainder_500+remainder_100+remainder_50+remainder_10)

