from services.phieumuonService import PhieumuonService
from services.sachService import SachService
from services.ordersService import OrdersService
from Exceptions.NotFound import NotFound
from libs.Helpers import processMenu, clear, showtable
from services.thanhvienService import ThanhvienService


class QuanlyPhieuMuon:
    def __init__(self, model):
        self.phieumuonService = PhieumuonService()
        self.ordersService = OrdersService()
        self.sachService = SachService()
        self.model = model
        self.thanhvienService = ThanhvienService()

    def taoPhieumuon(self):
        id_thanhvien = input("Nhập id thành viên: ")
        try:
            self.thanhvienService.find(id_thanhvien)
        except NotFound:
            print("Mã thành viên không tồn tại !")
        else:
            tiencoc = 0
            list_sach = []
            while True:
                try:
                    clear()
                    showtable(self.sachService.dict_tableFull())
                    ma_sach = input("Nhập mã sách: ")
                    sach = self.sachService.find(ma_sach)
                    list_sach.append(sach)
                    tiencoc += sach.get("giatri")
                except NotFound:
                    print("Sách này không có trong thư viện")
                menu = processMenu({
                    1: "Mượn thêm sách",
                    2: "Hoàn tất"
                })
                if menu == 2:
                    break
            hanCuoi = self.phieumuonService.giahan()
            phieumuon = self.phieumuonService.themPhieuMuon(id_thanhvien, self.model.id_nhanvien, tiencoc, hanCuoi)
            for sach in list_sach:
                self.ordersService.store({
                    "id_phieumuon": self.phieumuonService.getlast(),
                    "id_sach": sach.get("id_sach")
                })



    def menuPhieuMuon(self):
        while True:
            menu = processMenu({
                1: "Thêm phiếu mượn",
                2: "Trả sách",
                3: "Tra cứu thông tin phiếu mượn",
                4: "Thống kê tiền",
                0: "Quay lại"
            })
            if menu == 1:
                clear()
                self.taoPhieumuon()
            elif menu == 2:
                clear()
                id_phieumuon = input("Nhập id phiếu mượn: ")
                self.phieumuonService.traSach(id_phieumuon)
            elif menu == 3:
                clear()
                fetch = self.phieumuonService.hethong_phieumuon()
                showtable(fetch)
                fetch_table = self.phieumuonService.traCuuPhieuMuon()
                try:
                    showtable(fetch_table)
                except:
                    print("Mã phiếu mượn không hợp lệ !")
                finally:
                    input("Xác nhận")
                    clear()
            elif menu == 4:
                sql = "select sum(TienCoc) as TongTienCoc, sum(TienPhat) as TongTienPhat from Phieumuon"
                self.phieumuonService.cursor.execute(sql)
                fetch = self.phieumuonService.cursor.fetchall()
                showtable(fetch)
                input("Xác nhận")
            elif menu == 0:
                break


