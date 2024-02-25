original_list = [1, 2, 3]
copied_list = original_list
copied_list.append(4)
print(original_list)  # [1, 2, 3, 4]

# original_list와 copied_list는 사실 같은 리스트
print(id(original_list), id(copied_list))