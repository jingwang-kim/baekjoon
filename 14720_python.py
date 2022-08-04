import sys
from urllib.parse import _ResultMixinBytes

#n = 우유 가게의 수, milk -> 0 = 딸기, 1 = 초코, 2 = 바나나
#규칙 : 딸기 -> 초코 -> 바나나 -> 딸기
n = int(sys.stdin.readline())
milk = list(map(int,sys.stdin.readline().split()))
result = 0
flag = 0
rule = [0,1,2]

for i in range(n):
    #규칙은 3개이므로 flag가 3이 넘어가면 다시 초기화
    if flag == 3:
        flag = 0
    
    #현재 flag에 있는 규칙으로 먹어야 하는 우유가 맞으면 result 증가
    if rule[flag] == milk[i]:
        result += 1
        flag += 1

print(result)