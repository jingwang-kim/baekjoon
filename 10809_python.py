import sys

s = sys.stdin.readline()
flag = 'abcdefghijklmnopqrstuvwxyz'

for i in flag:
    print(s.find(i))