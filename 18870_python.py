import sys

n = int(sys.stdin.readline())
coor = list(map(int,sys.stdin.readline().split())) #2 4 -10 4 -9

#좌표를 리스트 안에서 크기 순서로 정렬 (제일 작은 수부터 0번)

#같은 수는 같은 좌표값을 가지므로 집합으로 중복값을 없앰
coorset = set(coor) #2 4 -10 -9
arr = list(coorset) #2 4 -10 -9
arr.sort() #-10 -9 2 4

coordict = {}
for i in range(len(arr)):
    coordict[arr[i]] = i  #{-10 : 0, -9 : 1, 2 : 2, 4 : 3}
for i in coor:
    print(coordict[i], end = ' ') #2 3 0 3 1