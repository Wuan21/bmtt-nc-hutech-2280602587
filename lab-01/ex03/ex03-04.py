def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

#nhap tuple tu nguoi dung
input_tuple = eval(input("nhap tuple: "))
first, last = truy_cap_phan_tu(input_tuple)
#in ket qua
print(f"Phan tu dau tien va cuoi cung cua tuple la: {first} va {last}")