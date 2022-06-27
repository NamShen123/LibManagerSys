from services.BaseService import BaseService


class SachService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = 'sach'
        self.id = "id_sach"

