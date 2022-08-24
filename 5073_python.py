import sys

while True:
    arr = list(map(int,sys.stdin.readline().split()))
    if arr.count(0) == 3:
        break
    arr.sort(reverse = True)
    if arr[0] >= arr[1] + arr[2]:
        print('Invalid')
    elif len(set(arr)) == 1:
        print('Equilateral')
    elif len(set(arr)) == 2:
        print('Isosceles')
    elif len(set(arr)) == 3:
        print('Scalene')