# 모범답안
n = int(input())
result = 0

while n >= 0: # n이 음수가 나올경우도 있음
    if n % 5 == 0:
        result += (n // 5)
        print(result)
        break

    n -= 3 # 5로 나누어 떨어질때까지 계속 빼주기
    result += 1
else: # n이 음수가 나오면 즉, 위에의 부정이면
    print(-1)