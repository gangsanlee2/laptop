password = int(input('비밀번호를 입력해주세요 : '))

print('password의 값 : ', password)
encoding = password <<2
print('패스워드가 암호화 되었습니다 : ', encoding)
decoding = password >> 2
print('패스워드가 복호화 되었습니다 : ', decoding)