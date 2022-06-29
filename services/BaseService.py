from database import Database
from Exceptions.NotFound import NotFound

class BaseService:
    def __init__(self):
        self.conn = Database().getConnection()
        self.table = None
        self.id = None
        self.cursor = self.conn.cursor(dictionary=True, buffered=True)

    def getlast(self):
        sql = "select max({0}) as last from {1}".format(self.id, self.table)
        self.cursor.execute(sql)
        return self.cursor.fetchone().get("last")

    def dict_tableFull(self):
        sql = "select * from {0}".format(self.table)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result is None:
            raise NotFound
        return result

    def find(self, id, thanhphan = '*'):
        sql = "select {2} from {0} where {1} = %s".format(self.table, self.id, thanhphan)
        self.cursor.execute(sql, (id,))
        result = self.cursor.fetchone()
        if result is None:
            raise NotFound
        return result

    def count(self):
        sql = "SELECT count(*) as total FROM {0}".format(self.table)
        self.cursor.execute(sql)
        return self.cursor.fetchone().get("total")

    def store(self, dict_data):
        columns = ", ".join(list(dict_data.keys()))
        sql = "INSERT INTO {0}({1}) VALUES ({2})".format(self.table, columns, ", ".join(["%s"] * len(dict_data.keys())))
        values = tuple(dict_data.values())
        # print(values)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def findByField(self, field, value):
        sql = "SELECT * FROM {0} where {1} = %s".format(self.table, field)
        self.cursor.execute(sql, (value,))
        result = self.cursor.fetchone()
        if result is None:
            raise NotFound
        return result

    def timkiem(self, noidung, chitiet, thanhphan='*'):
        sql = "select {3} from {0} where {1} like '%{2}%'".format(self.table, noidung, chitiet, thanhphan)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result is None:
            raise NotFound
        return result

    def chinhsua(self, dict_sua, dict_dieukien):
        cot_sua, noidung_sua = list(dict_sua.items())[0]
        cot_dk, noidung_dk = list(dict_dieukien.items())[0]
        sql = "UPDATE {0} SET {1} = %s WHERE {2} = %s".format(self.table, cot_sua, cot_dk)
        self.cursor.execute(sql, (noidung_sua, noidung_dk))
        self.conn.commit()



# a = [{"key1": "val1a", "key2": "val2a"}, {"key1": "val1b", "key2": "val2b"}, {"key1": "val1c", "key2": "val2c"}]
# b = Convert_to_list()
# b.listdict_to_list(a)
# print(b.header)
# print(b.body)
