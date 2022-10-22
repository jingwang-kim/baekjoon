import sys

k = int(sys.stdin.readline())
arr=[]
max_width = 0
w_idx = 0
max_height = 0
h_idx = 0

for i in range(6):
    tmp = list(map(int,sys.stdin.readline().split()))
    arr.append(tmp)

    #1 = 동, 2 = 서, 3 = 남, 4 = 북
    if tmp[0] == 1 or tmp[0] == 2:
        if max_width < tmp[1]:
            max_width = tmp[1]
            w_idx = i
    else:
        if max_height < tmp[1]:
            max_height = tmp[1]
            h_idx = i

# %6 하는 방법을 생각하지 못함
min_w = abs(arr[(h_idx+1)%6][1] - arr[(h_idx-1)%6][1])
min_h = abs(arr[(w_idx+1)%6][1] - arr[(w_idx-1)%6][1])
result = ((max_width * max_height) - (min_w * min_h)) * k
print(result)