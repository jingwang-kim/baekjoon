import sys
'''
1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''
n = int(sys.stdin.readline())
color=[]

for _ in range(n):
    color.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    color[i][0] += min(color[i-1][1], color[i-1][2])
    color[i][1] += min(color[i-1][0], color[i-1][2])
    color[i][2] += min(color[i-1][0], color[i-1][1])

print(min(color[n-1]))