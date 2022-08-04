import sys

#n = 사람의 수, data = 각 사람의 예상 등수, real = 실제 등수
n = int(sys.stdin.readline().strip())
data = [0] * n
real = [0] * n

for i in range(n):
    data[i] = int(sys.stdin.readline().strip()) #ex) 1 5 3 1 2
    real[i] = i+1                               #ex) 1 2 3 4 5

data.sort()                                     #ex) 1 1 2 3 5
result = 0

for j in range(n):
    result += abs(data[j] - real[j])            #ex) 0 1 1 1 0

print(result)