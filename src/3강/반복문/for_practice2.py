files = ["2024_A사.xlsx", "2021_B사.xlsx", "2023_A사.xlsx", "2022_B사.xlsx"]

company_a = []
company_b = []

for fname in files:
    # "A사"라는 글자가 fname에 포함되어 있으면 True, 그렇지 않으면 False를 반환합니다.
    if "A사" in fname:
        company_a.append(fname)
    else:
        company_b.append(fname)

print("A사 자료 :", company_a)
print("B사 자료 :", company_b)