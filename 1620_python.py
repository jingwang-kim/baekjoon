import sys

n,m = map(int,sys.stdin.readline().split())

pokemon = {}
for i in range(1,n+1):
    tmp = sys.stdin.readline().rstrip()
    pokemon[i] = tmp
    pokemon[tmp] = i

for i in range(m):
    search = sys.stdin.readline().rstrip()
    #isdigit : 문자열이 숫자로만 이루어졌는지 판단
    #모든 문자가 숫자이면 True
    if search.isdigit():
        print(pokemon[int(search)])
    else:
        print(pokemon[search])