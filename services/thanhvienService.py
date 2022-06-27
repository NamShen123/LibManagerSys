from services.BaseService import BaseService


class ThanhvienService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = 'thanhvien'
        self.id = "id_thanhvien"

    def themThanhvien(self, Ho_va_ten, Namsinh, Phone, Dia_chi = ""):
        sql = "insert into {0}(Ho_va_ten, Namsinh, Phone, Dia_chi) value (%s, %s, %s, %s)".format(self.table)
        self.cursor.execute(sql, (Ho_va_ten, Namsinh, Phone, Dia_chi))
        self.conn.commit()
        print("Đã cập nhật vào cơ sở dữ liệu !")




