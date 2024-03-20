x = int(input("Nhập một giá trị cho x: "))
try:
    assert x < 1, 'x không nhỏ hơn 1'
except AssertionError as e:
    print(f"Lỗi xác nhận: {e}")
