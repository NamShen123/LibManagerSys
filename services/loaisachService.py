from services.BaseService import BaseService


class LoaisachService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = 'loaisach'
        self.id = 'id_loaisach'

