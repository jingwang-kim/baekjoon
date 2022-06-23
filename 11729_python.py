import sys
# 1 -> 2, 1 -> 3, 2 -> 3, 
def hanoi(n, start, middle, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n - 1, start, end, middle)
    print(start, end)
    hanoi(n-1, middle, start, end)


n = int(sys.stdin.readline())
print(2**n-1)
hanoi(n,1,2,3)