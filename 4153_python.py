import sys

while True:
    triangle = list(map(int,sys.stdin.readline().split()))
    if triangle.count(0) == 3:
        break
    triangle.sort()
    if triangle[2]**2 == (triangle[1]**2 + triangle[0]**2):
        print('right')
    else:
        print('wrong')