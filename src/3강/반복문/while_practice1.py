cart = []

while len(cart) < 5:
    product = input("카트에 넣을 상품을 입력해주세요 : ")
    if not product:
        print("잘못된 입력입니다.")
    else:
        cart.append(product)
        print(f"카트에 {product}를 담았습니다.")

print("카트가 가득 찼습니다. 프로그램을 종료합니다.")
print(f"카트에 담긴 물품 : {cart}")