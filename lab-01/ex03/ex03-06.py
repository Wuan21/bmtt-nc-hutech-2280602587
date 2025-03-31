def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
#su dung ham va in ket qua
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_delete = "b"
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("Dictionary sau khi xoa: ", my_dict)
else:
    print("khong tim thay phan tu can xoa trong dictionary.")