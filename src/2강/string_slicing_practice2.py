# 문자열 정의
text = "Python Programming"

# 2개 문자마다 점프하여 추출하기
print("2개 문자마다 점프:", text[::2])

# 문자열 뒤집기
print("문자열 뒤집기:", text[::-1])

# 문자열 뒤집기 (심화)
print("문자열 뒤집기:", text[:6:-1])
# (추가)작동 방식
# text[:6:-1]
# None은 slicing에서 끝을 의미하며 두번째 : 뒤의 숫자의 부호에 따라 앞쪽인지 뒤쪽인지 결정
# = text[None:6:-1] 
# (두번째 : 뒤의 숫자가 음수이기 때문에 None은 문자열의 끝인 17번째 index에서 시작)
# = text[17:6:-1]