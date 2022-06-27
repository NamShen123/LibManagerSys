from services.BaseService import BaseService
from libs.Helpers import md5
from models.Nhanvien import Nhanvien
from Exceptions.WrongAccount import WrongAccount
from Exceptions.NotFound import NotFound


class NhanvienService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = "nhanvien"
        self.id = "id_nhanvien"

    def checklogin(self, taikhoan, matkhau):
        matkhau = md5(matkhau)
        sql = "select * from {0} where {1} = %s and {2} = %s".format(self.table, 'taikhoan', 'matkhau')
        self.cursor.execute(sql, (taikhoan, matkhau))
        result = self.cursor.fetchone()
        if result is None:
            raise WrongAccount
        return Nhanvien(result)

    def kiemtraTaikhoan(self, taikhoan):
        sql = "select * from {0} where taikhoan = %s".format(self.table)
        self.cursor.execute(sql, (taikhoan, ))
        result = self.cursor.fetchone()
        if result is None:
            return False
        return True

    def themNhanhvien(self, Ho_va_ten, taikhoan, matkhau, Role="Nhân viên"):
        matkhau_ = md5(matkhau)
        sql = "insert into {0}(Ho_va_ten, taikhoan, matkhau, Role) value (%s, %s, %s, %s)".format(self.table)
        self.cursor.execute(sql, (Ho_va_ten, taikhoan, matkhau_, Role))
        self.conn.commit()
        print("Đã cập nhật vào cơ sở dữ liệu !")






