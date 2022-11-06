money = int(input('돈을 넣어주세요 : '))
count = int(input('몇 장 드릴까요? : '))
ticket = 1200

money -= (ticket*count)
print('거스름돈 :', money)