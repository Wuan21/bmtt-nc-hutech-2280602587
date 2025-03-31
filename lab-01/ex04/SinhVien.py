class SinhVien:
    def __init__(self, svId, name, sex, major, diemTB):
        self._id = svId
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = "" 

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getSex(self):
        return self._sex

    def getMajor(self):
        return self._major

    def getDiemTB(self):
        return self._diemTB

    def getHocLuc(self):
        return self._hocLuc
