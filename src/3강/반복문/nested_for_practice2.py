# 버블 정렬 (Bubble sort) : 인접한 요소끼리 비교하여 교환하는 과정을 통해 정렬하는 방식
numbers = [5, 3, 2, 6, 10, 1]

# len() 함수는 리스트나 문자열과 같은 시퀀스 데이터의 길이를 반환합니다.
for i in range(len(numbers) - 1, -1, -1):
    for j in range(i):
        if numbers[j+1] < numbers[j]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("정렬 결과 :", numbers)