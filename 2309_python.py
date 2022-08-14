import sys

hobit = []
for _ in range(9):
    hobit.append(int(sys.stdin.readline()))
flag = sum(hobit) - 100

for i in range(8):
    for j in range(i+1,len(hobit)):
        if (hobit[i] + hobit[j]) == flag:
            n = hobit[i]
            m = hobit[j]
            
hobit.remove(n)
hobit.remove(m)
hobit.sort()

for k in hobit:
    print(k)