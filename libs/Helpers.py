import hashlib
from prettytable import PrettyTable
import os


def md5(istr):
    result = hashlib.md5(istr.encode())
    return result.hexdigest()


def showtable(dict_table):
    if type(dict_table) == type(list()):
        table = PrettyTable(list(dict_table[0].keys()))
        for ele_row in dict_table:
            table.add_row(list(ele_row.values()))
        print(table)
    elif type(dict_table) == type(dict()):
        table = PrettyTable(list(dict_table.keys()))
        table.add_row(list(dict_table.values()))
        print(table)



def alert(message):
    lengthStr = len(message)
    print('='*lengthStr)
    print(message)
    print('='*lengthStr)


def processMenu(menus):
    while True:
        print("Nhập lựa chọn")
        for key in menus.keys():
            print(str(key) + ': ' + menus[key])
        menu = int(input(""))
        if menu in list(menus.keys()):
            return menu
        alert("Hãy nhập giá trị hợp lệ !")


def clear():
    os.system("cls")
