original_list = [1, 2, 3]
copied_list = original_list.copy() # 리스트를 제대로 복사하는 방법!
copied_list.append(4)
print(original_list)  # [1, 2, 3, 4]

# original_list와 copied_list는 다른 리스트
print(id(original_list), id(copied_list))