import sys

#ababc
#abc   --> 오류
#str = ['aba', 'bc\n']

text = sys.stdin.readline()
search = sys.stdin.readline().strip()

index = 0
result = 0

#index가 text - search 길이보다 커지면 중단( ex> ababababa , aba )
while index <= len(text) - len(search):  #len(text) - len(search) -> 9-3 = 6
    if search == text[index:index+len(search)]:
        result += 1
        index += len(search)
    else:
        index += 1

print(result)