s = input().upper() #MISSISSIPI
flag = list(set(s)) #M I S P
arr = []            #1 4 4 1

for i in flag:
    cnt = s.count(i)
    arr.append(cnt)

if arr.count(max(arr)) > 1:
    print('?')
else:
    result = arr.index(max(arr))
    print(flag[result])