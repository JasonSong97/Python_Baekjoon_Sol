# 1
extra_money = 1000 - int(input())
coin_lst = [500, 100, 50, 10, 5, 1]
result = 0

for coin in coin_lst:
    result += extra_money // coin
    extra_money = extra_money % coin

print(result)