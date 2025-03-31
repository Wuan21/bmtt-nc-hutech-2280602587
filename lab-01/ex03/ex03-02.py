def dao_nguoc_list(lst):
    return lst[::-1]

#nhap danh sach tu nguoi dung va su ly chuoi
input_list = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))

#su dung ham va in ket qua
list_dao_nguoc = dao_nguoc_list(numbers)
print("List dao nguoc la: ", list_dao_nguoc)