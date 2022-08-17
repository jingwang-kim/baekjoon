cnt = 1
selnum = []

while cnt <= 10000:
    tmp =list(map(int,str(cnt)))
    selnum.append(cnt + sum(tmp))
    if cnt not in selnum:
        print(cnt)
    cnt += 1