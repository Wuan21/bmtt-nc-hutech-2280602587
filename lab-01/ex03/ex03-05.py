def dem_so_lan_xuat_hien(s, c):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

#nhap danh sach tu nguoi dung
input_string = input("nhap danh sach cac tu, cach nhau boi dau cach: ")
word_list = input_string.split()

#su dung ham va in ket qua
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua cac tu la: ", so_lan_xuat_hien)