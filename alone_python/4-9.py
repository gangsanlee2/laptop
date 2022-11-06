print('===== 자판기 메뉴 =====')
print('1.음료 1000원  2.과자 2000원  3.껌 500원')
print()

cracker = 2000
drink = 1000
ggum = 500
money = int(input('Insert coin : '))

if money >= cracker:
    print('과자, 음료, 껌 모두 구매할 수 있습니다.')
elif money < cracker and money >= drink:
    print('음료, 껌 구매할 수 있습니다.')
elif money <drink and money >=ggum:
    print('껌 구매할 수 있습니다.')
elif money < ggum:
    print('금액이 모자랍니다.')
else:
    print('입력값이 잘못되었습니다')
