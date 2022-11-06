id = 'jamsuham75'
pw = '1234'

userid = input('사용자아이디 : ')
userpw = input('사용자비밀번호 : ')

if id == userid:
    if pw == userpw:
        print('로그인 되었습니다')
    else:
        print('비밀번호가 틀렸습니다')
else:
    print('아이디가 틀렸습니다')