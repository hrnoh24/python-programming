my_tuple = (1, 2, 3)
my_list = list(my_tuple)  # 튜플을 리스트로 변환
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

my_new_tuple = tuple(my_list)  # 리스트를 튜플로 변환
print(my_new_tuple)  # (1, 2, 3, 4)
