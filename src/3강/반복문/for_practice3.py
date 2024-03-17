students_score_map = {"노ㅇㅇ" : 10, "유ㅇㅇ" : 55, "김ㅇㅇ" : 23, "고ㅇㅇ" : 74, "김XX" : 100}

# dictionary 자료형의 items()를 이용하면 key와 value를 for문 내에서 사용할 수 있습니다.
# for name, score in students_score_map.items():
#     if score >= 80:
#         print(f"{name} 학생의 학점은 A입니다.")
#     elif score >= 60:
#         print(f"{name} 학생의 학점은 B입니다.")
#     elif score >= 40:
#         print(f"{name} 학생의 학점은 C입니다.")
#     elif score >= 20:
#         print(f"{name} 학생의 학점은 D입니다.")
#     else:
#         print(f"{name} 학생의 학점은 F입니다. 당장 나가세요.")

for item in students_score_map.items():
    print(item)

for name, score in students_score_map.items():
    print(name, score)

item = ('노ㅇㅇ', 10)
item = ('유ㅇㅇ', 55)

name, score = ('노ㅇㅇ', 10)
name, score = ('유ㅇㅇ', 55)