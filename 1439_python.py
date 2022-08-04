import sys

s = sys.stdin.readline()
cnt = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt+=1
        
result = (cnt)//2
print(result)