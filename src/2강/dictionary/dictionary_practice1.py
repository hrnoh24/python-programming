# 딕셔너리 생성
person = {"name": "John", "age": 30}

# 딕셔너리에서 값 접근
print("Name:", person["name"])
print("Age:", person["age"])

# 주의할 점: 존재하지 않는 키에 접근하려 할 때
# 안전하게 접근하기 위해 get 메소드 사용
print("Gender:", person.get("gender", "Not specified"))