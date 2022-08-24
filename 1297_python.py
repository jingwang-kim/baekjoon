import sys
import math

d,h,w = map(int,sys.stdin.readline().split())

r = d/math.sqrt(h**2 + w**2)
print(int(h*r), int(w*r))