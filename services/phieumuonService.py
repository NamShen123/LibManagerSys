from services.BaseService import BaseService
from Exceptions.NotFound import NotFound

class PhieumuonService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = 'phieumuon'
        self.id = 'id_phieumuon'

    def themPhieuMuon(self, id_thanhvien, id_nhanvien, tiencoc, hanCuoi):
        sql = '''insert into {0}(id_thanhvien, TinhTrang, id_nhanvien, TienCoc, HanChot) value (%s, %s, %s, %s, %s)'''.format(self.table)
        self.cursor.execute(sql, (id_thanhvien, 'DM', id_nhanvien, tiencoc, hanCuoi))
        self.conn.commit()

    def giahan(self):
        sql = "select adddate(current_timestamp, INTERVAL 90 day) as hanCuoi"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        hanCuoi = result['hanCuoi']
        return hanCuoi

    def kiemTraHan(self, id_phieumuon):
        result = self.chenhlechNgay(id_phieumuon)
        return int(result) < 0

    def chenhlechNgay(self, id_phieumuon):
        sql = "select datediff(NgayTra, HanChot) as ThoiGian from {0} where {1} = %s".format(self.table, self.id)
        self.cursor.execute(sql, (id_phieumuon,))
        result = self.cursor.fetchone()
        return result['ThoiGian']

    def traSach(self, id_phieumuon):
        try:
            phieu = self.find(id_phieumuon)
        except NotFound:
            print("Mã phiếu mượn không hợp lệ")
        else:
            tinhtrang = phieu.get('TinhTrang')
            if tinhtrang != "DM":
                print("Phiếu đã trả rồi!")
                input("Xác nhận")
            else:
                sql = "update {0} set Ngaytra = current_timestamp(), TienCoc = 0 where {1} = %s".format(self.table, self.id)
                self.cursor.execute(sql, (id_phieumuon,))
                self.conn.commit()
                if self.kiemTraHan(id_phieumuon):
                    tinhTrang = "DT"
                else:
                    tinhTrang = "QH"
                    SoNgayQuaHan = self.chenhlechNgay(id_phieumuon)
                    TienPhat = SoNgayQuaHan * 500
                    sql = "update {0} set SoNgayQuaHan = %s, TienPhat = %s where {1} = %s".format(self.table, self.id)
                    self.cursor.execute(sql, (SoNgayQuaHan, TienPhat, id_phieumuon))
                    self.conn.commit()
                sql = "update {0} set TinhTrang = %s where {1} = %s".format(self.table, self.id)
                self.cursor.execute(sql, (tinhTrang, id_phieumuon))
                self.conn.commit()

    def traCuuPhieuMuon(self):
        try:
            id_phieumuon = input("Nhập mã phiếu mượn: ")
            sql = "select sach.id_sach, sach.Ten_sach, sach.giatri, orders.id_phieumuon from sach inner join orders on sach.id_sach = orders.id_sach and orders.id_phieumuon = %s"
            self.cursor.execute(sql, (id_phieumuon,))
            result = self.cursor.fetchall()
            return result
        except Exception:
            print("Mã phiếu mượn không hợp lệ !")
            input("Enter để quay lại !")

    def hethong_phieumuon(self):
        sql = "select * from {0}".format(self.table)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

