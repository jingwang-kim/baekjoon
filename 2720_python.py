import sys

t = int(sys.stdin.readline())

for i in range(t):
    money = int(sys.stdin.readline())

    quarter = money // 25
    money = money % 25

    dime = money // 10
    money = money % 10

    nickel = money // 5
    money = money % 5

    penny = money // 1
    money = money % 1

    print(quarter, dime, nickel, penny)