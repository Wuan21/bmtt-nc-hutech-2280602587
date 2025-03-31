from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateId(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def nhapSinhVien(self):
        svId = self.generateId()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính: ")
        major = input("Nhập ngành học: ")
        diemTB = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính: ")
            major = input("Nhập ngành học: ")
            diemTB = float(input("Nhập điểm trung bình: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai")
        
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
        
    def findByID(self, ID):
        return next((sv for sv in self.listSinhVien if sv._id == ID), None)
    
    def findByName(self, name):
        return [sv for sv in self.listSinhVien if name.lower() in sv._name.lower()]
    
    def xoaSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False
    
    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"
    
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<18} {:<18} {:<18} {:<18}".format("ID", "Tên", "Giới tính", "Ngành học", "Điểm trung bình", "Học lực"))
        for sv in listSV:
            print("{:<8} {:<18} {:<18} {:<18} {:<18} {:<18}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")
    
    def getListSinhVien(self):
        return self.listSinhVien
    
    def soLuongSinhVien(self):
        return len(self.listSinhVien)
