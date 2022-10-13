# 1
n = int(input())
a=[]
for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)
new_a=[]

for i in range(n):
    new_a.append(a[i]*(i+1))

new_a.sort()
print(new_a[n-1])

# 2
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
result = []

for i in l:
    result.append(i*n)
    n -=1

print(max(result))