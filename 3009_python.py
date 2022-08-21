import sys

list_x = []
list_y = []
result_x = 0
result_y = 0

for _ in range(3):
    x,y = map(int,sys.stdin.readline().split())
    list_x.append(x)
    list_y.append(y)

for i in range(3):
    if list_x.count(list_x[i]) % 2 !=0:
        result_x = list_x[i]
    if list_y.count(list_y[i]) % 2 !=0:
        result_y = list_y[i]

print(result_x,result_y)