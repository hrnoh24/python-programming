# 리스트에서 딕셔너리 생성
names = ["Alice", "Bob", "Charlie"]
ages = [24, 27, 22]

# 딕셔너리 내포 사용
name_age_dict = {name: age for name, age in zip(names, ages)}
print(name_age_dict)

# 주의할 점: 딕셔너리 키는 유일해야 한다. 중복되면 마지막 값으로 덮어쓰여진다.