favorite = int(input('내가 가장 좋아하는 숫자는? '))
start = int(input('범위 시작값 : '))
end = int(input('범위 끝값 : '))

for i in range(start,end+1,1):
    if favorite == i:
        print('내가 좋아하는 숫자가 있습니다')