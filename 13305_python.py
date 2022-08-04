import sys

n = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split()))
gas = list(map(int,sys.stdin.readline().split()))

cost = 0
mini = gas[0]
for i in range(n-1):
    if gas[i] < mini:
        mini = gas[i]
    cost += mini * road[i]
print(cost)