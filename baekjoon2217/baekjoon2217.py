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