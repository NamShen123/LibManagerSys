from services.nhanvienService import NhanvienService
from Exceptions.WrongAccount import WrongAccount
from function.quanlyPhieuMuon import QuanlyPhieuMuon
from function.quanlyThanhVien import QuanlyThanhvien
from function.quanlyNhanVien import QuanlyNhanVien
from function.thongtinCanhan import ThongtinCanhan
from function.quanlySach import QuanlySach
from libs.Helpers import clear


print("chạy trên terminal, tk: admin, mk: 123qwe")

class Main:
    clear()
    currentUser = None

    def __init__(self):
        self.nhanvien = NhanvienService()

    def process(self):
        print("Thư viện 4.0 xin chào!")
        if self.currentUser is None:
            return self.login()
        # print("Thư viện 4.0 xin chào!")
        self.showMenu()

    @staticmethod
    def message(string):
        len_string = len(string)
        print('='*len_string)
        print(string)
        print('='*len_string)

    def login(self):
        taikhoan = input('Nhập tài khoản: ')
        matkhau = input('Nhập mật khẩu: ')
        # taikhoan = 'admin'
        # matkhau = 'admin'
        try:
            self.currentUser = self.nhanvien.checklogin(taikhoan, matkhau)
        except WrongAccount:
            clear()
            self.message("Tài khoản hoặc mật khẩu sai !")
        self.process()

    def showMenu(self):
        clear()
        print("Xin chào, " + self.currentUser.Ho_va_ten)
        if self.currentUser.isAdminsator():
            return self.quanlyMenu()
        return self.nhanvienMenu()

    def processMenuOption(self, option):
        if option == 1:
            self.Phieumuon()
        elif option == 2:
            self.Thanhvien()
        elif option == 3:
            self.CaNhan()
        elif option == 4:
            self.Sach()
        elif option == 5:
            self.Nhanvien()
        elif option == 0:
            clear()
            print("Phiên làm việc kết thúc!")

    def Phieumuon(self):
        phieumuon = QuanlyPhieuMuon(self.currentUser)
        phieumuon.menuPhieuMuon()
        clear()
        self.process()

    def Thanhvien(self):
        thanhvien = QuanlyThanhvien(self.currentUser)
        thanhvien.menuQuanlyThanhVien()
        clear()
        self.process()

    def Nhanvien(self):
        nhanvien = QuanlyNhanVien(self.currentUser)
        nhanvien.menuQuanlyNhanVien()
        clear()
        self.process()

    def CaNhan(self):
        canhan = ThongtinCanhan(self.currentUser)
        canhan.menuThongtinCanhan()
        clear()
        self.process()

    def Sach(self):
        sach = QuanlySach(self.currentUser)
        sach.menuQuanlySach()
        clear()
        self.process()

    def nhanvienMenu(self):
        menus = {
            1: "Quản lý phiếu mượn",
            2: "Quản lý thành viên",
            3: "Thông tin cá nhân",
            4: "Quản lý sách",
            0: "Đăng xuất"
        }
        menuOption = self.processMenu(menus)
        self.processMenuOption(menuOption)

    def quanlyMenu(self):
        clear()
        menus = {
            1: "Quản lý phiếu mượn",
            2: "Quản lý thành viên",
            3: "Thông tin cá nhân",
            4: "Quản lý sách",
            5: "Quản lý nhân viên",
            0: "Đăng xuất"
        }
        menuOption = self.processMenu(menus)
        clear()
        self.processMenuOption(menuOption)

    def processMenu(self, dict_menus):
        while True:
            print("Tuỳ chọn")
            for key in dict_menus.keys():
                print(str(key) + ": " + dict_menus[key])
            option = int(input(""))
            if option in dict_menus.keys():
                return option
            self.message("Tuỳ chọn không xác định, hãy nhập lại !")

Main().process()

