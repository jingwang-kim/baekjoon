import sys

a,b = map(int,sys.stdin.readline().split())
set_a = set(map(int,sys.stdin.readline().split()))
set_b = set(map(int,sys.stdin.readline().split()))

print(len(set_a-set_b) + len(set_b-set_a))