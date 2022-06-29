from services.sachService import SachService
from libs.convert_to_list import Convert_to_list
from libs.Helpers import clear, processMenu, showtable
from Exceptions.NotFound import NotFound
from services.loaisachService import LoaisachService
from matplotlib import pyplot
# import numpy as np

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
                4: "Xu hướng đọc sách",
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
            elif menu == 4:
                clear()
                self.thongKeLuotMuon()


            elif menu == 0:
                break

    def thongKeLuotMuon(self):
        sql = """select Ten_loai as "Thể loại", count(Ten_loai) as "Lượt mượn" from orders, sach, loaisach
                where orders.id_sach = sach.id_sach and sach.id_loaisach = loaisach.id_loaisach
                group by Ten_loai
                order by count(Ten_loai) desc;"""

        self.sachService.cursor.execute(sql)
        fetch = self.sachService.cursor.fetchall()
        theloai_luotmuon = Convert_to_list()
        theloai_luotmuon.listdict_to_list(fetch)
        theloai = list(x[0] for x in theloai_luotmuon.body)
        luotmuon = list(map(int, list(x[1] for x in theloai_luotmuon.body)))

        pyplot.pie(luotmuon, labels=theloai, explode= [0.1] + [0]*(len(luotmuon)-1))
        pyplot.legend(title="Thể loại")
        pyplot.show()

        print("Chủ đề {}, {} đang được đọc giả quan tâm nhiều nhất".format(theloai[0], theloai[1]))
        print("Trong đó: ")
        print("{0} đã cho mượn {1} quyển".format(theloai[0], luotmuon[0]))
        print("{0} đã cho mượn {1} quyển".format(theloai[1], luotmuon[1]))
        input("Xác nhận")
        clear()

