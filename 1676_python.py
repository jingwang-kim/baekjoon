import sys

#팩토리얼에서 0의 개수는 5개 몇개 있냐에 따라 결정된다
#예를 들어, 10!에서 5가 나오는 경우는 5와 10(2*5) 가 있으므로 0의 개수는 2가 되는 것이다
n = int(sys.stdin.readline())

result = 0

while n >= 5:
    result += n//5
    n//=5
print(result)
