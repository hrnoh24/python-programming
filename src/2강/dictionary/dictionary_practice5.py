# 중첩 딕셔너리 생성
person = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}

# 중첩된 값 접근
print("City:", person["address"]["city"])

# 주의할 점: 깊은 중첩은 접근 및 수정 시 실수를 유발할 수 있으니 주의해야 한다.
