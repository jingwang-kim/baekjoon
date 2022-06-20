import sys

t = int(sys.stdin.readline())

cnt_a = t//300
cnt_b = (t%300)//60
cnt_c = ((t%300)%60)//10

if t % 10 !=0:
    print(-1)
else:
    print(cnt_a, cnt_b, cnt_c)