from BaseService import BaseService


class NopPhatService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = 'NopPhat'
        self.id = "id_nopphat"
