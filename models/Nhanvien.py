class Nhanvien:
    def __init__(self, dict_data):
        self.id_nhanvien = dict_data.get('id_nhanvien')
        self.Ho_va_ten = dict_data.get('Ho_va_ten')
        self.taikhoan = dict_data.get('taikhoan')
        self.matkhau = dict_data.get('matkhau')
        self.Role = dict_data.get('Role')

    def isAdminsator(self):
        return self.Role == "Quản lý"

