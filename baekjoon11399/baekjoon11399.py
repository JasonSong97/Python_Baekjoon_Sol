# 1
n = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0
sub_1 = 0
sub_2 = n

while True:
    result += p[sub_1]*sub_2
    if sub_2 == 1:
        print(result)
        break
    sub_1 += 1
    sub_2 -= 1

# 2
n = int(input())
a = list(map(int, input().split()))

time = 0
a.sort()

for i in range(n): # n 번 실행
    for j in range(i + 1): # 
        time += a[j]
print(time)