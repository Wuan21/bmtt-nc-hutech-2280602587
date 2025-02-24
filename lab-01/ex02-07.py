#nhap du lieu tu nguoi dung
print("Nhap thu cai gi vao day di(done de kthuc): ")
lines = []
while True:
    line = input()
    if line == "done":
        break
    lines.append(line)
    #Chuyen cac dong thanh chu in hoa va in ra man hinh
    print("\n Cac dong da nhap sau khi chuyen thanh chu in hoa: ")
    for line in lines:
        print(line.upper())