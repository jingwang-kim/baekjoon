import sys
from collections import Counter

n = int(sys.stdin.readline())

def find_mode(result):
    c = Counter(result)
    order = c.most_common()
    maxi = order[0][1]

    modes = []
    for i in order:
        if i[1] == maxi:
            modes.append(i[0])
    return sorted(modes)

def find_median(result):
    med = len(result) // 2
    if len(result) % 2 == 0: #짝수일 때
        return (result[med] + result[med-1]) // 2
    else:
        return result[med]
result = []
for _ in range(n):
    result.append(int(sys.stdin.readline()))
result.sort()
modes = find_mode(result)

print(int(round(sum(result)/n,0)))
print(find_median(result))

if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])

print(int(max(result) - min(result)))