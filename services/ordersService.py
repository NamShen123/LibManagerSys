from services.BaseService import BaseService


class OrdersService(BaseService):
    def __init__(self):
        super().__init__()
        self.table = 'orders'

