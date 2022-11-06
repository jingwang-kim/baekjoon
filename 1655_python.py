import sys
import heapq

'''
ex) [1, 5, 2, 10, -99, 7, 5]
num = 1 👉🏻 left = [-1] / right = []
num = 5 👉🏻 left = [-1], right = [5]
num = 2 👉🏻 left = [-2,-1], right = [5]
num = 10 👉🏻 left = [-2,-1], right = [5,10]
num = -99 👉🏻 left = [-2,-1,99], right = [5,10]
num = 7 👉🏻 left = [-2,-1,99], right = [5,7,10]
num = 5 👉🏻 left = [-5,-2,-1,99], right = [5,7,10]
'''

n = int(sys.stdin.readline())
#left에는 중간값보다 작은수, right에는 중간값보다 큰 수
#left는 최대힙, right는 최소 힙
l_hq = [] #여기에 중간값이 있어야 함(짝수일 경우 left에서 출력하면 되기 때문)
r_hq = []

for i in range(n):
    x = int(sys.stdin.readline())

    #길이 같으면 중간값의 기준을 맟추기 위해 left에 넣는다
    #길이가 다르면 길이를 맟춰주기 위해 right에 넣는다
    if len(l_hq) == len(r_hq):
        heapq.heappush(l_hq,-x)
    else:
        heapq.heappush(r_hq,x)

    #right에 값을 넣는 차례에 left보다 작은 값을 넣으면 right에 중간값보다
    #큰 원소가 들어가므로 left와 right의 첫 원소를 교체
    if r_hq and -l_hq[0] > r_hq[0]:
        left = heapq.heappop(l_hq)
        right = heapq.heappop(r_hq)

        heapq.heappush(l_hq,-right)
        heapq.heappush(r_hq,-left)
    
    print(-l_hq[0])