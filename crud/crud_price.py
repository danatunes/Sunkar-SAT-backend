from app.crud.base import CRUDBase
from app.models import Price
from app.schemas import PriceUpdate, PriceCreate


class CRUDPrice(CRUDBase[Price, PriceCreate, PriceUpdate]):
    pass


price = CRUDPrice(Price)
