import sys

n,m = map(int,sys.stdin.readline().split())

n_list = [] #포함되어있는 문자열
m_list = [] #n_list에 있는지 검사하는 문자열
result = 0

for _ in range(n):
    n_list.append(sys.stdin.readline())

for _ in range(m):
    m_list.append(sys.stdin.readline())

for i in m_list:
    if i in n_list:
        result += 1

print(result)
