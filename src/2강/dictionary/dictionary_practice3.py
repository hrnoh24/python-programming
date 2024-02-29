# 딕셔너리 생성
person = {"name": "John", "age": 30}

# 모든 키-값 쌍 순회
for key, value in person.items():
    print(f"{key}: {value}")

# 주의할 점: 딕셔너리는 순서를 보장하지 않는다. Python 3.7+부터는 삽입 순서를 보장한다.
