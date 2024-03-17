# 삽입 정렬 (Insertion sort) : 앞에서부터 차례대로 이미 정렬된 부분과 비교하여 교환하는 방식
numbers = [5, 3, 2, 6, 10, 1]

for i in range(1, len(numbers)):
    for j in range(i, 0, -1):
        if numbers[j] < numbers[j-1]:
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]

print("정렬 결과 :", numbers)