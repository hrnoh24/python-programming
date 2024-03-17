user_input = int(input("숫자를 입력하세요 :"))

is_prime = True
for 숫자 in range(2, user_input):
    if user_input % 숫자 == 0:
        is_prime = False

if is_prime:
    print(f"{user_input}은 소수입니다.")
else:
    print(f"{user_input}은 소수가 아닙니다.")
