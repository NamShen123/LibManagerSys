from services.nhanvienService import NhanvienService
from libs.Helpers import processMenu, showtable, clear, md5

class ThongtinCanhan:
    def __init__(self, model):
        self.model = model
        self.nhanvienService = NhanvienService()

    def menuThongtinCanhan(self):
        while True:
            clear()
            menu = processMenu({
                1: "Xem thông tin cá nhân",
                2: "Đổi mật khẩu",
                3: "Đổi tên",
                0: "Quay lại"
            })
            if menu == 1:
                clear()
                fetch = self.nhanvienService.find(str(self.model.id_nhanvien), thanhphan="id_nhanvien, Ho_va_ten, taikhoan, Role")
                showtable(fetch)
                input("xác nhận")
            elif menu == 2:
                clear()
                matkhauCu = input("Nhập mật khẩu cũ: ")
                if md5(matkhauCu) == self.model.matkhau:
                    matkhau = input("nhập mật khẩu mới: ")
                    confirm_matkhau = input("nhập lại mật khẩu mới: ")
                    if matkhau == confirm_matkhau:
                        matkhau = md5(matkhau)
                        self.nhanvienService.chinhsua({"matkhau": matkhau}, {"id_nhanvien": str(self.model.id_nhanvien)})
                        input("Xác nhận")
                        clear()
                    else:
                        print("Xác nhận không trùng khớp !")
                        input("Xác nhận")
                        clear()
                else:
                    print("Mật khẩu sai!")
                    input("xác nhận")
                    clear()
            elif menu == 3:
                ten = input("Nhập tên mới: ")
                self.nhanvienService.chinhsua({"Ho_va_ten": ten}, {"id_nhanvien": str(self.model.id_nhanvien)})
                fetch = self.nhanvienService.find(self.model.id_nhanvien)
                showtable(fetch)
                input("Xác nhận")
                clear()
            elif menu == 0:
                break


