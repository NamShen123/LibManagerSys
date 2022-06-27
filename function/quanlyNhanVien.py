from services.nhanvienService import NhanvienService
from libs.Helpers import showtable, clear, processMenu
from Exceptions.NotFound import NotFound


class QuanlyNhanVien:
    def __init__(self, model):
        self.model = model
        self.nhanvienService = NhanvienService()

    def menuQuanlyNhanVien(self):
        while True:
            menu = processMenu({
                1: "Thêm nhân viên",
                2: "Tra cứu nhân viên",
                3: "Cập nhật nhân viên",
                0: "Quay lại"
            })
            if menu == 1:
                taikhoan = input("Nhập tài khoản mới: ")
                if self.nhanvienService.kiemtraTaikhoan(taikhoan):
                    print("tài khoản đã tồn tại")
                    input("xác nhận")
                    clear()
                else:
                    matkhau = input("Nhập mật khẩu: ")
                    confirm_matkhau = input("Nhập lại mật khẩu: ")
                    if matkhau == confirm_matkhau:
                        Ho_va_ten = input("Nhập họ tên: ")
                        self.nhanvienService.themNhanhvien(Ho_va_ten,taikhoan,matkhau)
                        input("Xác nhận")
                        clear()
                    else:
                        print("Mật khẩu không trùng khớp")
                        input("xác nhận")
                        clear()
            elif menu == 2:
                Ho_va_ten = input("Nhập tên nhân viên: ")
                try:
                    fetch = self.nhanvienService.timkiem("Ho_va_ten", Ho_va_ten, thanhphan="id_nhanvien, Ho_va_ten, taikhoan, Role")
                except NotFound:
                    print("Không có kết quả tìm kiếm phù hợp!")
                    input("xác nhận")
                    clear()
                else:
                    showtable(fetch)
            elif menu == 3:
                clear()
                option = processMenu({
                    1: "Sửa tên",
                    2: "Thăng/giáng chức vụ"
                })
                if option == 1:
                    id_nhanvien = input("Nhập id nhân viên: ")
                    try:
                        self.nhanvienService.find(id_nhanvien)
                    except NotFound:
                        print("Mã nhân viên không tồn tại")
                        input("xác nhận")
                        clear()
                    else:
                        noidung = input("Nhập tên mới: ")
                        self.nhanvienService.chinhsua({"Ho_va_ten": noidung}, {"id_nhanvien": id_nhanvien})
                        fetch = self.nhanvienService.find(id_nhanvien)
                        showtable(fetch)
                        input("Xác nhận")
                        clear()
                elif option == 2:
                    next_option = processMenu({
                        1: "Thăng chức",
                        2: "Giáng chức"
                    })
                    if next_option == 1:
                        id_nhanvien = input("nhập id nhân viên: ")
                        try:
                            self.nhanvienService.find(id_nhanvien)
                        except NotFound:
                            print("Mã nhân viên không hợp lệ!")
                            input("Xác nhận")
                            clear()
                        else:
                            if id_nhanvien == str(self.model.id_nhanvien):
                                print("Không thể tự cập nhật chức vụ cho bản thân !")
                                input("Xác nhận")
                                clear()
                            else:
                                self.nhanvienService.chinhsua({"Role": "Quản lý"}, {"id_nhanvien": id_nhanvien})
                                fetch = self.nhanvienService.find(id_nhanvien)
                                showtable(fetch)
                                input("Xác nhận")
                                clear()
                    elif next_option == 2:
                        id_nhanvien = input("nhập id nhân viên: ")
                        try:
                            self.nhanvienService.find(id_nhanvien)
                        except NotFound:
                            print("Mã nhân viên không hợp lệ!")
                            input("Xác nhận")
                            clear()
                        else:
                            if id_nhanvien == str(self.model.id_nhanvien):
                                print("Không thể tự cập nhật chức vụ cho bản thân !")
                                input("Xác nhận")
                                clear()
                            else:
                                self.nhanvienService.chinhsua({"Role": "Nhân viên"}, {"id_nhanvien": id_nhanvien})
                                fetch = self.nhanvienService.find(id_nhanvien)
                                showtable(fetch)
                                input("Xác nhận")
                                clear()

            elif menu == 0:
                break


    # def

