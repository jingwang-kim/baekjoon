import sys
import math

score = []
for _ in range(5):
    score.append(int(sys.stdin.readline()))
score.sort()
print(sum(score)//5)
print(score[2])