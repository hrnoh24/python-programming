# 난수 생성을 위한 함수를 가지고 있는 패키지를 임포트합니다.
import random

# 0 ~ 50까지의 숫자 중 하나를 랜덤하게 반환합니다.
answer = random.randint(0, 50)

while True:
    user_input = int(input("정수를 입력해주세요 :"))

    if user_input < answer:
        print("Up!")
    elif user_input > answer:
        print("Down!")
    else:
        print("정답입니다!")
        break