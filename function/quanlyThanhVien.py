from services.thanhvienService import ThanhvienService
from Exceptions.NotFound import NotFound
from libs.Helpers import showtable, processMenu, clear
# from matplotlib import pyplot
from libs.convert_to_list import Convert_to_list

class QuanlyThanhvien:
    def __init__(self, model):
        self.thanhvienService = ThanhvienService()
        self.model = model

    def kiemtraThanhvien(self, id_thanhvien):
        # dang tra nguoc gia tri, tam dung not
        try:
            self.thanhvienService.find(id_thanhvien)
        except NotFound:
            return False
        else:
            return True

    def thongtinThanhVien(self):
        clear()
        id_thanhvien = input("Nhập mã thành viên: ")
        if self.kiemtraThanhvien(id_thanhvien):
            result = self.thanhvienService.find(id_thanhvien)
            showtable(result)
        else:
            print("Thành viên không tồn tại")

    def checkPhone(self, phone):
        clear()
        try:
            self.thanhvienService.findByField("Phone", phone)
        except NotFound:
            return True
        else:
            return False

    def menuQuanlyThanhVien(self):
        while True:
            menu = processMenu({
                1: "Thêm thành viên",
                2: "Tra cứu thông tin thành viên",
                3: "Cập nhật thông tin thành viên",
                4: "Thể loại sách yêu thích",
                0: "Quay lại"
            })
            if menu == 1:
                clear()
                phone = input("Nhập số điện thoại đăng ký: ")
                if self.checkPhone(phone):
                    Ho_va_ten = input("Nhập tên của thành viên: ")
                    Namsinh = input("Nhập ngày thàng năm sinh <YYYY-MM-DD>: ")
                    diachi = input("Nhập địa chỉ: ")
                    self.thanhvienService.themThanhvien(Ho_va_ten,Namsinh,phone,diachi)
                    fetch = self.thanhvienService.findByField("Phone", phone)
                    showtable(fetch)
                else:
                    print("Số điện thoại đã tồn tại !")
                    input("Xác nhận")
            elif menu == 2:
                clear()
                option = processMenu({
                    1: "Theo mã thành viên",
                    2: "Theo họ tên thành viên",
                    3: "Theo năm sinh",
                    4: "Theo điện thoại",
                    5: "Theo địa chỉ"
                })
                if option == 1:
                    clear()
                    fetch = self.thanhvienService.findByField("id_thanhvien", input("Nhập mã thành viên: "))
                    showtable(fetch)
                elif option == 2:
                    clear()
                    noidung = 'Ho_va_ten'
                    chitiet = input("tên tìm kiếm: ")
                    try:
                        fetch = self.thanhvienService.timkiem(noidung=noidung, chitiet=chitiet)
                    except NotFound:
                        print("Không có thông tin trùng khớp !")
                    else:
                        showtable(fetch)
                        input('xác nhận')
                        clear()
                elif option == 3:
                    clear()
                    noidung = 'Namsinh'
                    chitiet = input("Năm sinh: ")
                    try:
                        fetch = self.thanhvienService.timkiem(noidung=noidung, chitiet=chitiet)
                    except NotFound:
                        print("Không có thông tin trùng khớp !")
                    else:
                        showtable(fetch)
                        input('xác nhận')
                        clear()
                elif option == 4:
                    clear()
                    noidung = 'Phone'
                    chitiet = input("số điện thoại: ")
                    try:
                        fetch = self.thanhvienService.timkiem(noidung=noidung, chitiet=chitiet)
                    except NotFound:
                        print("Không có thông tin trùng khớp !")
                    else:
                        showtable(fetch)
                        input('xác nhận')
                        clear()
                elif option == 5:
                    clear()
                    noidung = 'Dia_chi'
                    chitiet = input("Địa chỉ tìm kiếm: ")
                    try:
                        fetch = self.thanhvienService.timkiem(noidung=noidung, chitiet=chitiet)
                    except NotFound:
                        print("Không có thông tin trùng khớp !")
                    else:
                        showtable(fetch)
                        input('xác nhận')
                        clear()
            elif menu == 3:
                clear()
                option = processMenu({
                    1: "Sửa tên",
                    2: "Cập nhật năm sinh",
                    3: "Cập nhật địa chỉ"
                })
                if option == 1:
                    id_thanhvien = input("Nhập id thành viên: ")
                    if not self.kiemtraThanhvien(id_thanhvien):
                        print("Mã thành viên không tồn tại")
                        return input("xác nhận")
                    noidung = input("Nhập tên mới: ")
                    self.thanhvienService.chinhsua({"Ho_va_ten": noidung}, {"id_thanhvien": id_thanhvien})
                    fetch = self.thanhvienService.find(id_thanhvien)
                    showtable(fetch)
                    input("Xác nhận")
                    clear()
                elif option == 2:
                    id_thanhvien = input("Nhập id thành viên: ")
                    if not self.kiemtraThanhvien(id_thanhvien):
                        print("Mã thành viên không tồn tại")
                        return input("xác nhận")
                    noidung = input("Nhập năm sinh <YYYY-MM-DD>: ")
                    self.thanhvienService.chinhsua({"Namsinh": noidung}, {"id_thanhvien": id_thanhvien})
                    fetch = self.thanhvienService.find(id_thanhvien)
                    showtable(fetch)
                    input("Xác nhận")
                    clear()
                elif option == 3:
                    id_thanhvien = input("Nhập id thành viên: ")
                    if not self.kiemtraThanhvien(id_thanhvien):
                        print("Mã thành viên không tồn tại")
                        return input("xác nhận")
                    noidung = input("Nhập địa chỉ mới: ")
                    self.thanhvienService.chinhsua({"Dia_chi": noidung}, {"id_thanhvien": id_thanhvien})
                    fetch = self.thanhvienService.find(id_thanhvien)
                    showtable(fetch)
                    input("Xác nhận")
                    clear()
            elif menu == 4:
                clear()
                self.theloaiSachyeuthich(input("Nhập id thành viên: "))
            elif menu == 0:
                break

    def theloaiSachyeuthich(self, id_thanhvien):
        sql = """select Ten_loai, count(Ten_loai) as "Lượt mượn"
                from thanhvien, phieumuon, orders, sach, loaisach
                where thanhvien.id_thanhvien = %s and thanhvien.id_thanhvien = phieumuon.id_thanhvien and phieumuon.id_phieumuon = orders.id_phieumuon and orders.id_sach = sach.id_sach and sach.id_loaisach = loaisach.id_loaisach
                group by Ten_loai
                order by count(Ten_loai) desc;"""
        self.thanhvienService.cursor.execute(sql, (id_thanhvien,))
        fetch = self.thanhvienService.cursor.fetchone()
        # print(fetch)
        tenloai_luotmuon = Convert_to_list()
        tenloai_luotmuon.listdict_to_list(fetch, lst=False)
        # tenloai = tenloai_luotmuon.header[0]
        tenloai = tenloai_luotmuon.body[0]

        thanhvien = self.thanhvienService.find(id_thanhvien)
        ten_thanhvien = thanhvien.get("Ho_va_ten")
        print("Thế loại sách yêu thích của {0} là {1}".format(ten_thanhvien, tenloai))
        input("Xác nhận")
        clear()


