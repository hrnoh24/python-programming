user_input = int(input("정수를 입력해주세요 :"))

answer = 10
if user_input < answer:
    print("Up!")
elif user_input > answer:
    print("Down!")
else:
    print("정답입니다!")