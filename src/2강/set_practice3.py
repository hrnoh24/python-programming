a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 교집합
print(a & b)  # {3, 4}

# 합집합
print(a | b)  # {1, 2, 3, 4, 5, 6}

# 차집합
print(a - b)  # {1, 2}

# 대칭 차집합 (합집합 - 교집합)
print(a ^ b)  # {1, 2, 5, 6}
