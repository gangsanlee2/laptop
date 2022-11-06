money = int(input('돈을 넣어주세요 : '))
count = int(input('몇 장 드릴까요? : '))
ticket = 1200

money -= (ticket*count)
change = '거스름돈 : ' + str(money)
result = money < 0 and '잔액이 부족합니다. 금액을 투입해주세요.' or change
print(result)