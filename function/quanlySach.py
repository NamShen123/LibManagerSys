from services.sachService import SachService
from libs.Helpers import clear, processMenu, showtable
from Exceptions.NotFound import NotFound
from services.loaisachService import LoaisachService

class QuanlySach:
    def __init__(self, model):
        self.model = model
        self.sachService = SachService()
        self.loaisach = LoaisachService()

    def menuQuanlySach(self):
        while True:
            menu = processMenu({
                1: "Thêm sách",
                2: "Sửa sách",
                3: "Tìm sách",
                0: "Quay lại"
            })
            if menu == 1:
                clear()
                self.sachService.cursor.execute("select * from loaisach")
                fetch = self.sachService.cursor.fetchall()
                showtable(fetch)

                Ten_sach = input("Nhập tên sách: ")
                giatri = input("Nhập giá tiền: ")
                if giatri.isdigit():
                    id_loaisach = input("Nhập mã loại sách: ")
                    try:
                        self.sachService.store({"Ten_sach": Ten_sach, "giatri": giatri, "id_loaisach": id_loaisach})
                        print("Cập nhật thành công !")
                        clear()
                    except:
                        print("Mã loại sách không hợp lệ")
                        input("Xác nhận")
                        clear()
            elif menu == 2:
                clear()
                id_sach = input("Nhập mã sách cần cập nhật: ")
                try:
                    self.sachService.find(id_sach)
                except NotFound:
                    print("Mã sách không tồn tại")
                    input("Xác nhận")
                    clear()
                else:
                    option = processMenu({
                        1: "sửa tên",
                        2: "sửa giá trị",
                        3: "sửa mã thể loại"
                    })
                    if option == 1:
                        noidung = input("Nhập tên sách mới: ")
                        self.sachService.chinhsua({"Ten_sach": noidung}, {"id_sach": id_sach})
                        self.sachService.conn.commit()
                        input("Xác nhận")
                        clear()
                    if option == 2:
                        noidung = input("Nhập giá tiền mới: ")
                        if noidung.isdigit():
                            self.sachService.chinhsua({"Ten_sach": noidung}, {"id_sach": id_sach})
                            self.sachService.conn.commit()
                            input("Xác nhận")
                            clear()
                        else:
                            print("Giá tiền không hợp lệ !")
                            input("Xác nhận")
                            clear()
                    if option == 3:
                        id_loaisach = input("Nhập mã loại sách: ")
                        try:
                            self.sachService.find(id_loaisach)
                        except NotFound:
                            print("Mã loại sách không tồn tại")
                            input("Xác nhận")
                            clear()
                        else:
                            self.sachService.chinhsua({"id_loai": id_loaisach}, {"id_sach": id_sach})
                            self.sachService.conn.commit()
                            input("Xác nhận")
                            clear()
            elif menu == 3:
                clear()
                option = processMenu({
                    1: "Theo tên sách",
                    2: "Thể loại"
                })
                if option == 1:
                    clear()
                    fetch = self.sachService.timkiem("Ten_sach", input("Nhập tên sách: "))
                    showtable(fetch)
                    input("Xác nhận")
                    clear()

                elif option == 2:
                    clear()
                    list_loaisach = self.loaisach.timkiem("Ten_loai", input("Nhập thể loại: "), thanhphan="id_loaisach")
                    str_dieukien = ''
                    for loaisach in list_loaisach:
                        str_dieukien += str("id_loaisach = '{0}' or").format(loaisach["id_loaisach"])
                    dieukien = str_dieukien[:-2]
                    sql = "select * from sach where {0}".format(dieukien)
                    self.sachService.cursor.execute(sql)
                    result = self.sachService.cursor.fetchall()
                    showtable(result)
                    input("xác nhận")
                    clear()
            elif menu == 0:
                break

