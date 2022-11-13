import sys

check = list(map(int,sys.stdin.readline().split()))

if sorted(check) == check:
    print('ascending')
elif sorted(check, reverse=True) == check:
    print('descending')
else:
    print('mixed')