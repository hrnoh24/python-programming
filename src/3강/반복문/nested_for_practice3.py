# 선택 정렬 (Selection sort)
# 최솟값을 찾아서 맨 앞으로 이동하는 방식
numbers = [5, 3, 2, 6, 10, 1]

for i in range(len(numbers)):
    min_idx = i
    
    # 리스트에서 가장 작은 숫자의 index를 찾습니다.
    for j in range(i+1, len(numbers)):
        if numbers[min_idx] > numbers[j]:
            min_idx = j
    
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print("정렬 결과 :", numbers)