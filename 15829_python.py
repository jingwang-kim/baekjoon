import sys

l = int(sys.stdin.readline())
str = list(sys.stdin.readline().rstrip())

flag = 31
result = 0

for i in range(l):
    #ord('a') - 96
    tmp = ord(str[i]) - 96
    result += tmp * (flag**i)

# 해시 함수의 정의에서 유한한 범위의 출력을 가져야 한다고 했으므로 M을 나누어 출력한다.
print(result% 1234567891)