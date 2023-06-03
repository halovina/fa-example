
from crud.base import CRUDBase
from models.customers import Customers

class CRUDCustomers(CRUDBase[Customers]):
    pass

customers = CRUDCustomers(Customers)

    