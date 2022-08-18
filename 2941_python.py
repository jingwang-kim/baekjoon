s = input()
result = 0
flag = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=','z=']
k = 0

for i in flag:
    if i in s:
        if s.count(i) > 1:
            result += s.count(i)
            s = s.replace(i,' ')
        else:
            s = s.replace(i,' ')
            result += 1

s=s.replace(' ','')
result += len(s)
print(result)
