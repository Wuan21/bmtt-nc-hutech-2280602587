def tao_tuple_tu_list(lst):
    return tuple(lst)

#nhap danh sach tu nguoi dung va su ly chuoi
input_list = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("list la: ", numbers)
print("Tuple tu list la: ", my_tuple)