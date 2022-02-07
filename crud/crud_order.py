from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import User
from app.models.order import Order
from app.schemas import UserRole
from app.schemas.order import OrderCreate, OrderUpdate, OrderStage


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    def create(self, db: Session, *, obj_in: OrderCreate) -> Order:
        obj_in_dict = obj_in.dict()
        obj_in_dict['stage'] = OrderStage.PENDING_ASSESSMENT
        db_obj = Order(**obj_in_dict)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def is_privileged(self, user: User) -> bool:
        return user.role == UserRole.ADMIN or user.role == UserRole.MANAGER


order = CRUDOrder(Order)
