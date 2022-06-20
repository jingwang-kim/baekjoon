import sys

a,b = sys.stdin.readline().split()
ans_min = int(a.replace('6','5')) + int(b.replace('6','5'))
ans_max = int(a.replace('5','6')) + int(b.replace('5','6'))
print(ans_min, ans_max)