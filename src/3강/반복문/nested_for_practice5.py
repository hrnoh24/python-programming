height = int(input("층 수를 입력하세요 :"))

for i in range(1, height + 1):
    for _ in range(height - i):
        print(" ", end="")

    for _ in range(i*2 - 1):
        print("*", end="")
    print("")
