import sys

n = int(sys.stdin.readline())
result = 0

if n < 100:
    print(n)

else:
    result = 99

    for i in range(100,n+1):
        arr = list(map(int,str(i)))

        if arr[0]-arr[1] == arr[1] - arr[2]:
            result += 1

    print(result)
