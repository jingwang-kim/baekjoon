n,k = map(int,input().split())
result = 0
list_m = []
for i in range(n):
    a = int(input())
    list_m.append(a)
list_m.reverse()

for i in list_m:
    result += k//i
    k = k % i
    
print(result)