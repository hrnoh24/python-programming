# 중복 값을 포함한 리스트
my_list = [1, 2, 2, 3, 4, 4, 5]

# 리스트를 set으로 변환하여 중복 제거
my_set = set(my_list)
print(my_set)  # {1, 2, 3, 4, 5} 출력

# 필요한 경우, 다시 리스트로 변환
my_list_no_duplicates = list(my_set)
print(my_list_no_duplicates)  # [1, 2, 3, 4, 5] 출력