month = int(input('월을 입력하세요 : '))

if month == 12 or month < 3 and month > 0 :
    print('겨울')
elif month > 2 and month < 6 :
    print('봄')
elif month > 5 and month < 9 :
    print('여름')
elif month > 8 and month < 12 :
    print('가을')
else:
    print('입력값이 잘못되었습니다.')
