# 리스트 요소 삭제 예시
desserts = ["스콘", "휘낭시에", "조각케잌", "탕후루"]
print(desserts)

# 특정 위치 삭제하기
del(desserts[2])
print("del(desserts[2])")
print(desserts)

# 범위 삭제
del(desserts[1:3])
print("del(desserts[1:3])")
print(desserts)
