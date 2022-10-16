# 1
T = int(input())
coin_type = [25, 10, 5, 1]
count = [0] * 4

for i in range(T):
    money = int(input())
    for j in range(len(coin_type)):
        count[j] += money // coin_type[j]
        money %= coin_type[j]
    print(' '.join(map(str, count)))

# 2
for _ in range(int(input())):
    C = int(input())
    d = [25, 10, 5, 1]
    li = []
    for n in d:
        li.append(C//n)
        C = C%n
    print(*li, sep = ' ') # *는 리스트의 대괄호 제거

# 3
T = int(input())
coins = [25, 10, 5, 1]
for _ in range (T):
    chg = int(input())
    for c in coins :
        n = chg // c
        chg %= c
        print(n, end=" ")